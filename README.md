# IMPLEMENTING-GRAPH-COLORING-PROBLEM-USING-BACKTRACKING-APPROACH
Graph coloring also called Vertex coloring is a process of assigning colors to all the vertices of the graph such that no two adjacent vertices of it are assigned the same color. In other words, there must not be any edge in the graph whose end vertices are colored with the same color. Such a graph is called a properly colored graph. 

The minimum number of colors required to color any graph such that no two adjacent vertices of it are assigned the same color is called Chromatic Number. Unfortunately, there is no efficient algorithm available for coloring a graph with a minimum number of colors as the problem is a known NP-Complete problem. Our goal is to find the chromatic number for a given graph with n vertices by using the backtracking approach.

The graph coloring problem has a huge number of applications like Making Schedule or Time Table where the minimum number of time slots is equal to the chromatic number of the graph, solving sudoku puzzles, map coloring i.e. Four colors are sufficient to color any map, register allocation for compiler optimization and mobile frequency assignment.

This projects is divided into two parts:\
1)Basic implementation of Graph Coloring Problem.\
2)Map Coloring implementation

# Algorithm
1.Detecting all non-white regions (eg. provinces or states).\
2.Converting the input map to a simple planar graph: There will be a node for each region. Two nodes will be adjacent, if and only if their corresponding regions have a common border on the map.\
3.Using backtracking for coloring that graph (it's a recursive function that produces all valid colorings).\
4.Displaying all produced colorings on the given map.

# Dependencies
pip install -r dependencies.txt

# Run
python3 map_coloring.py map_image_file_name

# Notes
It runs slowly on large images.
