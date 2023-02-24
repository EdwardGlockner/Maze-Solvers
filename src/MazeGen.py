"""



"""
import random

class MazeGen():
    def __init__(self, width = 15, height = 15, seed = 1):
        self.width = width
        self.height = height
        self.seed = 1

        self.empty = " "
        self.mark = "@"
        self.wall = chr(9608)
        self.north, self.south, self.east, self.west = "n", "s", "e", "w"

        self.maze = {}
        for x in range(self.width):
            for y in range(self.height):
                self.maze[(x,y)] = self.wall # initiate with walls everywhere


    def print_maze(self, markX = None, markY = None):
        """


        """
        for y in range(self.height):
            for x in range(self.width):
                if markX == x and markY == y:
                    print(self.mark, end = " ")

                else:
                    print(self.maze[(x,y)], end = " ")
            print()
        

    def visit(self, x, y, hasVisited):
        """


        """
        self.maze[(x,y)] = self.empty
        self.print_maze(x,y)
        print("\n\n")

        while True:
            # Check which neighboring spaces adjacent to
            # the mark have not been visited already:
            unvisitedNeighbors = []
            if y > 1 and (x, y - 2) not in hasVisited:
                unvisitedNeighbors.append(self.north)

            if y < self.height - 2 and (x, y + 2) not in hasVisited:
                unvisitedNeighbors.append(self.south)

            if x > 1 and (x - 2, y) not in hasVisited:
                unvisitedNeighbors.append(self.west)

            if x < self.width - 2 and (x + 2, y) not in hasVisited:
                unvisitedNeighbors.append(self.east)

            if len(unvisitedNeighbors) == 0:
                # BASE CASE
                # All neighboring spaces have been visited, so this is a
                # dead end. Backtrack to an earlier space:
                return
            else:
                # RECURSIVE CASE
                # Randomly pick an unvisited neighbor to visit:
                nextIntersection = random.choice(unvisitedNeighbors)

                # Move the mark to an unvisited neighboring space:

                if nextIntersection == self.north:
                    nextX = x
                    nextY = y - 2
                    self.maze[(x, y - 1)] = self.empty # Connecting hallway.
                elif nextIntersection == self.south:
                    nextX = x
                    nextY = y + 2
                    self.maze[(x, y + 1)] = self.empty # Connecting hallway.
                elif nextIntersection == self.west:
                    nextX = x - 2
                    nextY = y
                    self.maze[(x - 1, y)] = self.empty # Connecting hallway.
                elif nextIntersection == self.east:
                    nextX = x + 2
                    nextY = y
                    self.maze[(x + 1, y)] = self.empty # Connecting hallway.

                hasVisited.append((nextX, nextY)) # Mark as visited.
                self.visit(nextX, nextY, hasVisited) # Recursively visit this space.

        

