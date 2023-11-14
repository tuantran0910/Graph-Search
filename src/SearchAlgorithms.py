from Space import *
from Constants import *
from time import *
import numpy as np
from queue import PriorityQueue

def DrawPath(g:Graph, ele:Node, father_ele:Node, sc:pygame.Surface, father):
    if ele == g.start:
        ele.set_color(orange)
        g.draw(sc)
        return 
    pygame.draw.line(sc, green, (ele.x, ele.y), (father_ele.x, father_ele.y), 3)
    ele.set_color(grey)
    g.draw(sc)
    if (ele == g.goal):
        ele.set_color(purple)
        g.draw(sc)
    return DrawPath(g, father_ele, g.grid_cells[father[father_ele.value]], sc, father)

def DFS(g:Graph, sc:pygame.Surface):
    open_set = [g.start.value] 
    closed_set = []
    father = [-1]*g.get_len()

    while len(open_set):
        start_vertex = open_set.pop()
        g.grid_cells[start_vertex].set_color(yellow)
        g.draw(sc)
        sleep(0.01)
        closed_set.append(start_vertex)
        g.grid_cells[start_vertex].set_color(blue)
        if g.is_goal(g.grid_cells[start_vertex]):
            g.grid_cells[start_vertex].set_color(purple)
            g.grid_cells[g.start.value].set_color(orange)
            DrawPath(g, g.grid_cells[start_vertex], g.grid_cells[father[start_vertex]], sc, father)
            g.draw(sc)
            return
        
        for adj_vertex in g.get_neighbors(g.grid_cells[start_vertex]):
            if adj_vertex.value not in closed_set:
                open_set.append(adj_vertex.value)
                father[adj_vertex.value] = start_vertex
                adj_vertex.set_color(red)
            
        g.draw(sc)
        sleep(0.01)
    
    raise NotImplementedError('Not implemented')
            

def BFS(g:Graph, sc:pygame.Surface):
    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    while len(open_set):
        element = open_set[0]
        g.grid_cells[element].set_color(yellow)
        g.draw(sc)
        closed_set.append(element)
        open_set.remove(element)
        g.grid_cells[element].set_color(blue)
        if g.is_goal(g.grid_cells[element]):
            g.grid_cells[element].set_color(purple)
            g.grid_cells[g.start.value].set_color(orange)  
            DrawPath(g, g.grid_cells[element], g.grid_cells[father[element]], sc, father)
            g.draw(sc)
            return
        
        for adj_vertex in g.get_neighbors(g.grid_cells[element]):
            if adj_vertex.value not in closed_set:
                open_set.append(adj_vertex.value)
                father[adj_vertex.value] = element
                adj_vertex.set_color(red)
                closed_set.append(adj_vertex.value)
        
        g.draw(sc)
                
    raise NotImplementedError('Not implemented')

def UCS(g:Graph, sc:pygame.Surface):
    open_set = PriorityQueue()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0 
    open_set.put((cost[g.start.value], g.start.value))
        
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    
    while not open_set.empty():
        (cost_value, node_value) = open_set.get()
        cost[node_value] = cost_value
        g.grid_cells[node_value].set_color(yellow)
        g.draw(sc)
        sleep(0.01)
        closed_set.append(node_value)
        g.grid_cells[node_value].set_color(blue)
        if (g.is_goal(g.grid_cells[node_value])):
            g.grid_cells[node_value].set_color(purple)
            g.grid_cells[g.start.value].set_color(orange)
            DrawPath(g, g.grid_cells[node_value], g.grid_cells[father[node_value]], sc, father)
            g.draw(sc)
            return
        
        for adj_vertex in g.get_neighbors(g.grid_cells[node_value]):
            if adj_vertex.value not in closed_set:
                if cost[adj_vertex.value] != 100_000:
                    temp = cost[adj_vertex.value]
                    new_cost = np.sqrt((adj_vertex.x - g.grid_cells[node_value].x) ** 2 + (adj_vertex.y - g.grid_cells[node_value].y) ** 2) + cost[node_value]
                    if temp > new_cost:
                        father[adj_vertex.value] = node_value
                        cost[adj_vertex.value] = new_cost
                        open_set.put((cost[adj_vertex.value], adj_vertex.value))
                        open_set.get(temp)
                else:
                    cost[adj_vertex.value] = np.sqrt((adj_vertex.x - g.grid_cells[node_value].x) ** 2 + (adj_vertex.y - g.grid_cells[node_value].y) ** 2) + cost[node_value]
                    open_set.put((cost[adj_vertex.value], adj_vertex.value))
                    father[adj_vertex.value] = node_value
                adj_vertex.set_color(red)
        g.draw(sc)
        sleep(0.01)

    #TODO: Implement UCS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')

def Dijkstra(g:Graph, sc:pygame.Surface):
    open_set = {}
    cost = [100_000] * g.get_len()
    cost[g.start.value] = 0
    
    for i in range(0, g.get_len()):
        open_set[i] = cost[i]
    open_set[g.start.value] = cost[g.start.value]
    closed_set:list[int] = []
    father = [-1] * g.get_len()

    while len(open_set):
        open_set = dict(sorted(open_set.items(), key = lambda x : x[1], reverse = True))
        node_value, cost[node_value] = open_set.popitem()
        g.grid_cells[node_value].set_color(yellow)
        g.draw(sc)
        sleep(0.01)
        closed_set.append(node_value)
        g.grid_cells[node_value].set_color(blue)
        
        if (g.is_goal(g.grid_cells[node_value])):
            g.grid_cells[node_value].set_color(purple)
            g.grid_cells[g.start.value].set_color(orange)
            g.draw(sc)
        
        for adj_vertex in g.get_neighbors(g.grid_cells[node_value]):
            if adj_vertex.value not in closed_set:
                if cost[adj_vertex.value] != 100_000:
                    temp = open_set[adj_vertex.value]
                    new_cost = np.sqrt((adj_vertex.x - g.grid_cells[node_value].x) ** 2 + (adj_vertex.y - g.grid_cells[node_value].y) ** 2) + cost[node_value]
                    if temp > new_cost:
                        father[adj_vertex.value] = node_value
                        cost[adj_vertex.value] = new_cost
                        open_set[adj_vertex.value] = cost[adj_vertex.value]
                else:
                    cost[adj_vertex.value] = np.sqrt((adj_vertex.x - g.grid_cells[node_value].x) ** 2 + (adj_vertex.y - g.grid_cells[node_value].y) ** 2) + cost[node_value]
                    open_set[adj_vertex.value] = cost[adj_vertex.value]
                    father[adj_vertex.value] = node_value
                adj_vertex.set_color(red)                    
        g.draw(sc)
        sleep(0.01)
    
    if (g.is_goal(g.grid_cells[g.goal.value])):   
        DrawPath(g, g.grid_cells[g.goal.value], g.grid_cells[father[g.goal.value]], sc, father)
        g.draw(sc)
        sleep(0.01)
        return
    
    raise NotImplementedError('Not implemented')
