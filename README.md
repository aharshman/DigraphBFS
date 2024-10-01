# Breadth-First Search (BFS) Implementation

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [How to Use](#how-to-use)
5. [Functions](#functions)
   - [BFS(graph, start, end, toPrint=False)](#bfsgraph-start-end-toprintfalse)
   - [printpath(path)](#printpathpath)
   - [testBFS()](#testbfs)
6. [Example Usage](#example-usage)
7. [Future Improvements](#future-improvements)
8. [License](#license)
9. [Author](#author)

## Overview

The Breadth-First Search (BFS) Implementation is a Python program that demonstrates the BFS algorithm on a directed graph. The program allows users to find the shortest path between two nodes in a graph using the BFS approach. This implementation is designed for educational purposes, showcasing how BFS can be applied to traverse graphs and find paths.

## Features

- **Shortest Path Finding**: Efficiently finds the shortest path from a starting node to an ending node in a directed graph.
- **Graph Representation**: Utilizes a `Digraph` class to represent the graph structure with nodes and edges.
- **Path Visualization**: Displays the current path during the search process for better understanding of the algorithm's progress.

## Requirements

- Python 3.x
- `digraph.py` file containing the `Digraph`, `Node`, and `Edge` classes.

## How to Use

1. Clone or download this repository.
2. Ensure the `digraph.py` file is available in the same directory as this script.
3. Run the script using Python:

    ```sh
    python bfs_implementation.py
    ```

4. The program will create a directed graph with nodes and edges, perform a BFS search, and display the shortest path.

## Functions

### `BFS(graph, start, end, toPrint=False)`

Performs a breadth-first search on the graph.

- **Inputs**: 
  - `graph`: An instance of the `Digraph` class.
  - `start`: The starting node for the search.
  - `end`: The target node to find the path to.
  - `toPrint`: Boolean indicating whether to print the current path during the search (default is `False`).
- **Outputs**: Returns the shortest path as a list of nodes if found; otherwise, returns `None`.

### `printpath(path)`

Generates a string representation of the path.

- **Inputs**: `path` - A list of nodes representing the path.
- **Outputs**: A formatted string displaying the path from start to end.

### `testBFS()`

Sets up a test scenario for the BFS algorithm.

- **Functionality**: Creates a directed graph, adds nodes and edges, and executes the BFS search, printing the results.

## Example Usage

To demonstrate the BFS functionality, run the script. The program will automatically create a directed graph, perform a BFS search, and print the shortest path from the specified starting node to the target node.

## Future Improvements

- **Enhanced Graph Visualization**: Implement a graphical representation of the graph for better clarity.
- **User Interaction**: Allow users to define their own nodes and edges through input.
- **Algorithm Variants**: Explore other graph traversal algorithms, such as Depth-First Search (DFS) and A* search.

## License

This project is open source and available under the MIT License.

## Author

**Author**: Alexa

Feel free to contribute or suggest improvements!
