import sys
import os 

sys.path.append(str(sys.path[0][:-14]))
dirname = os.getcwd()
sys.path.insert(1, os.path.join(dirname))

from MazeGen import MazeGen
from Graphics import Graphics

###
#Maze = MazeGen(width=10, height=10)
#hasVisited = [(1,1)]
#Maze.visit(1,1, hasVisited)
#Maze.print_maze()
#print(Maze.maze)

###

def main():
    Window = Graphics()
    Window.run_simulation()

if __name__ == "__main__":
    main()




