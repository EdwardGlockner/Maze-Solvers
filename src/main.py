import sys
import os 

sys.path.append(str(sys.path[0][:-14]))
dirname = os.getcwd()
sys.path.insert(1, os.path.join(dirname))

from MazeGen import MazeGen

Maze = MazeGen(width=40, height=40)
hasVisited = [(1,1)]
Maze.visit(1,1, hasVisited)
Maze.print_maze()

