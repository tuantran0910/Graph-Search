# Graph Search

## Introduction

> This practical final project is part of the Data Structures & Algorithms course in the field of Data Science at VNUHCM - University of Science.
> 
> The majority of the code for this project was provided by my lab instructor, Mr. Nguyen Bao Long. In this project, my main contribution is in the ```SearchAlgorithms.py``` file.

![image](https://github.com/TuanTran0910/Graph-Search/assets/94174684/a487c1b1-ff27-4bbb-9fd4-7393894d1255)

Graph search is the process of traversing or exploring a graph data structure to find a specific element or to solve a particular problem. A graph is a collection of nodes (vertices) connected by edges.

There are various algorithms and strategies for graph search:
- Breadth-First Search (BFS): This algorithm explores all the vertices at the same level before moving to the next level. It starts from a given source node and visits all its neighbors before moving to the next level of neighbors.
- Depth-First Search (DFS): DFS explores as far as possible along each branch before backtracking. It starts from a given source node and explores as deep as possible, visiting the first unvisited neighbor before backtracking.
- Uniform Cost Search (UCS): UCS is an uninformed search algorithm that explores the graph by considering the cost associated with each edge.
- Dijkstra's Algorithm: This algorithm is used to find the shortest path between two nodes in a weighted graph. It starts from a source node and iteratively selects the node with the minimum distance, updating the distances of its neighbors.

## Usage

### Installation

To install the correct version of Python (version 3.9.12 or higher) for this project, you can visit the following [link](https://www.python.org/downloads/release/python-3912/) to download and install.

Clone the project to your local machine:

```python
git clone https://github.com/TuanTran0910/Graph-Search.git
cd Graph-Search
```

To install the necessary libraries, you can use the following command:

```bash
pip install -r requirements.txt
```

### Search node in Graph

To run the searching process, we have to run this following command:

```python
python main.py --algo <algo> --start <start> --goal <goal>
```

Where,
- "--algo <algo>": This parameter specifies the algorithm ```algo``` to be used. There are four algorithms that can be used in this project (```DFS```, ```BFS```, ```UCS```, ```Dijkstra```)
- "--start <start>": This parameter specifies the starting node ```start``` or vertex for the graph search.
- "--goal <goal>": This parameter specifies the goal node ```goal``` or vertex that the search aims to reach.

For example, to perform a graph search using the Depth-First Search algorithm, starting from node 71 and aiming to reach node 318:

```python
python src/main.py --algo DFS --start 71 --goal 318
```

## Contribution

This project is a collaborative effort, and we would like to acknowledge the contributions of the following individual:
- Nguyen Hai Ngoc Huyen

I would like to express my gratitude to my teammate for her hard work and dedication to this project. Without her efforts, this project would not have been possible.
