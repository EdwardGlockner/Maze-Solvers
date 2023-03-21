"""


"""
import random

class MazeGen():
    def __init__(self, width = 30, height = 30, seed = 1):
        self.width = width
        self.height = height
        self.seed = seed
        self.maze = []

        self.mark = "mark"
        self.wall = "wall"
        self.cell = "cell"
        self.not_visited = "not_visited"

        for i in range(self.height):
            line = []
            for j in range(self.width):
                line.append(self.not_visited)
            self.maze.append(line)

       
    def _neighbor_cells(self, wall):
        neighbors = 0
        
        if self.maze[wall[0]-1][wall[1]] == self.cell:
            neighbors += 1
        if self.maze[wall[0]+1][wall[1]] == self.cell:
            neighbors += 1
        if self.maze[wall[0]][wall[1]-1] == self.cell:
            neighbors +=1
        if self.maze[wall[0]][wall[1]+1] == self.cell:
	        neighbors += 1

        return neighbors

    def generate(self):

        self.start_height = int(random.random() * self.height)
        self.start_width = int(random.random() * self.width)

        if (self.start_height == 0):
	        self.start_height += 1
        if (self.start_height == self.height-1):
            self.start_height -= 1
        if (self.start_width == 0):
            self.start_width += 1
        if (self.start_width == self.width-1):
            self.start_width -= 1


        # Mark it as cell and add surrounding walls to the list
        self.maze[self.start_height][self.start_width] = self.cell
        walls = []
        walls.append([self.start_height - 1, self.start_width])
        walls.append([self.start_height, self.start_width - 1])
        walls.append([self.start_height, self.start_width + 1])
        walls.append([self.start_height + 1, self.start_width])

        # Denote walls in maze
        self.maze[self.start_height-1][self.start_width] = self.wall 
        self.maze[self.start_height][self.start_width - 1] = self.wall
        self.maze[self.start_height][self.start_width + 1] = self.wall 
        self.maze[self.start_height + 1][self.start_width] = self.wall 

        while (walls):
            # Pick a random wall
            rand_wall = walls[int(random.random()*len(walls))-1]

            # Check if it is a left wall
            if (rand_wall[1] != 0):
                if (self.maze[rand_wall[0]][rand_wall[1]-1] == self.not_visited and self.maze[rand_wall[0]][rand_wall[1]+1] == self.cell):
                    # Find the number of surrounding cells
                    neighbor_cells = self._neighbor_cells(rand_wall)

                    if (neighbor_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = self.cell 

                        # Mark the new walls
                        # Upper cell
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != self.cell):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = self.wall 
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])


                        # Bottom cell
                        if (rand_wall[0] != self.height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != self.cell):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = self.wall
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])

                        # Leftmost cell
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != self.cell):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = self.wall 
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])


                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            # Check if it is an upper wall
            if (rand_wall[0] != 0):
                if (self.maze[rand_wall[0]-1][rand_wall[1]] == self.not_visited and self.maze[rand_wall[0]+1][rand_wall[1]] == self.cell):

                    neighbor_cells = self._neighbor_cells(rand_wall)
                    if (neighbor_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = self.cell 

                        # Mark the new walls
                        # Upper cell
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != self.cell):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = self.wall
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])

                        # Leftmost cell
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != self.cell):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = self.wall 
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])

                        # Rightmost cell
                        if (rand_wall[1] != self.width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != self.cell):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = self.wall 
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            # Check the bottom wall
            if (rand_wall[0] != self.height-1):
                if (self.maze[rand_wall[0]+1][rand_wall[1]] == self.not_visited and self.maze[rand_wall[0]-1][rand_wall[1]] == self.cell):

                    neighbor_cells = self._neighbor_cells(rand_wall)
                    if (neighbor_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = self.cell 

                        # Mark the new walls
                        if (rand_wall[0] != self.height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != self.cell):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = self.wall 
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != self.cell):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = self.wall 
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])
                        if (rand_wall[1] != self.width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != self.cell):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = self.wall 
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)


                    continue

            # Check the right wall
            if (rand_wall[1] != self.width-1):
                if (self.maze[rand_wall[0]][rand_wall[1]+1] == self.not_visited and self.maze[rand_wall[0]][rand_wall[1]-1] == self.cell):

                    neighbor_cells = self._neighbor_cells(rand_wall)
                    if (neighbor_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = self.cell 

                        # Mark the new walls
                        if (rand_wall[1] != self.width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != self.cell):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = self.wall 
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])
                        if (rand_wall[0] != self.height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != self.cell):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = self.wall 
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != self.cell):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = self.wall 
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            # Delete the wall from the list anyway
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)



            # Mark the remaining unvisited cells as walls
            for i in range(0, self.height):
                for j in range(0, self.width):
                    if (self.maze[i][j] == self.not_visited):
                        self.maze[i][j] = self.wall 

            # Set entrance and exit
            for i in range(0, self.width):
                if (self.maze[1][i] == self.cell):
                    self.maze[0][i] = self.cell 
                    break

            for i in range(self.width-1, 0, -1):
                if (self.maze[self.height-2][i] == self.cell):
                    self.maze[self.height-1][i] = self.cell
                    break
                

