# Graph Coloring Using Backtracking Algorithm

<p align="center">
  <img src="YOUR_IMAGE_LINK_HERE" width="600">
</p>

---

## 📌 Overview

This repository contains the implementation of the **Graph Coloring Problem using the Backtracking Algorithm** in Python.

The objective of this lab is to determine whether an undirected graph can be colored using **K colors** such that no two adjacent vertices have the same color.

The program reads graph information from an input file, applies the backtracking algorithm, and generates a valid color assignment if possible.

---

# 🎯 Objectives

- To understand the concept of the Graph Coloring problem.
- To implement the Backtracking algorithm for graph coloring.
- To check whether a graph can be colored using a given number of colors.
- To learn recursion and constraint checking techniques.
- To analyze the performance of the backtracking approach.

---

# 📝 Problem Statement

Given an undirected graph with **N vertices** and **M edges**, the task is to assign colors to the vertices using **K available colors**.

The condition is:

- No two adjacent vertices should have the same color.
- If a valid coloring exists, display the color assignment.
- Otherwise, display that coloring is not possible.

### Input Format

The first line contains:

```
N M K
```

Where:

- `N` = Number of vertices
- `M` = Number of edges
- `K` = Number of available colors

The next `M` lines contain edges:

```
u v
```

where `u` and `v` represent an undirected edge.

---

# ⚙️ Algorithm

The Graph Coloring problem is solved using the **Backtracking Algorithm**.

### Steps:

1. Start from the first vertex.
2. Try assigning each available color to the current vertex.
3. Check whether the selected color is safe.
4. If the color is valid, assign it and move to the next vertex.
5. If the assignment creates a conflict, remove the color.
6. Backtrack and try another possible color.
7. Continue until all vertices are colored or no solution exists.

---

# 🔹 Pseudocode

```
Algorithm Graph_Coloring(Graph, K)

Input:
    Graph with N vertices
    K = number of available colors

Output:
    Valid color assignment or failure


Function isSafe(vertex, color):

    For every adjacent vertex:

        If adjacent vertex has the same color:

            Return False

    Return True



Function ColorGraph(vertex):

    If all vertices are colored:

        Return True


    For each color from 1 to K:

        If color is safe:

            Assign color to vertex


            If ColorGraph(next vertex):

                Return True


            Remove color assignment
            (Backtracking)


    Return False
```

---

# 💻 Implementation Details

### Programming Language

```
Python
```

### Algorithm Used

```
Backtracking
```

### Data Structure

```
Adjacency Matrix
```

### Input Method

```
Text File (input.txt)
```

---

# 📂 Project Structure

```
Graph-Coloring-Backtracking
│
├── graphcoloring.py
│
├── input.txt
│
└── README.md
```

---

# 📥 Input Example

`input.txt`

```
2

4 5 3
0 1
0 2
1 2
1 3
2 3

4 5 2
0 1
0 2
1 2
1 3
2 3
```

---

# 📤 Output Example

```
Case #1:
Coloring Possible with 3 Colors
Color Assignment: [1, 2, 3, 1]

Case #2:
Coloring Not Possible with 2 Colors
```

---

# 📸 Output Screenshot

<p align="center">
  <img src="YOUR_OUTPUT_SCREENSHOT_LINK_HERE" width="700">
</p>

---

# 📊 Result

The implemented program successfully solves the Graph Coloring problem using the Backtracking algorithm.

For the first test case, the graph was successfully colored using 3 colors and generated the following valid color assignment:

```
[1, 2, 3, 1]
```

For the second test case, the algorithm correctly identified that coloring was not possible using only 2 colors.

---

# 💡 Discussion and Conclusion

In this lab, the Graph Coloring problem was implemented using the Backtracking algorithm. The algorithm assigns colors to vertices one by one and checks whether the assignment is valid. If a conflict occurs, it removes the previous assignment and tries another possible color.

The experiment demonstrates that backtracking is an effective technique for solving constraint-based problems. It successfully finds valid solutions when enough colors are available and detects impossible cases when the available colors are insufficient.

Although the algorithm provides an exact solution, its execution time increases for larger graphs because it explores multiple possible color combinations. The worst-case time complexity of this algorithm is:

```
O(K^N)
```

where:

- `K` = Number of available colors
- `N` = Number of vertices

Overall, this lab helped to understand recursion, constraint checking, and backtracking techniques for solving graph coloring problems.

---

# ⏱️ Complexity Analysis

## Time Complexity

```
O(K^N)
```

## Space Complexity

```
O(N^2)
```

because an adjacency matrix is used to represent the graph.

---

# 🛠️ How to Run

### Step 1: Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

### Step 2: Open Project Folder

```bash
cd Graph-Coloring-Backtracking
```

### Step 3: Run Python Program

```bash
python graphcoloring.py
```

---

# 👨‍💻 Author

**Your Name**

Department of Computer Science and Engineering
