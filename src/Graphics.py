#--IMPORTS-------------------------------------------------+
import pygame
import os
import time
import sys

#--FIXING PATHS -------------------------------------------+
sys.path.append(str(sys.path[0][:-14]))
dirname = os.getcwd()
sys.path.insert(1, os.path.join(dirname))

#--LOCAL IMPORTS-------------------------------------------+
from MazeGen import MazeGen

"""

"""

class Graphics():
    def __init__(self, width = 70, height = 70):
        """


        """
        # Define colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        
        # Define properties of the 2D array
        self.width = width
        self.height = height
        self.win_width = 800
        self.win_height = 800
        self.margin = 5 # Margin between each cell
        self.cell_size = self.win_width/self.width


        # Define properties of the window
        pygame.init()
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        pygame.display.set_caption('Line Test')

        # Define the maze object
        self.MazeObj = MazeGen(self.width, self.height)
        hasVisited = [(1,1)]
        self.MazeObj.visit(1,1, hasVisited)

        # Testing, but iterate over the self.maze object
        

        self.running = False

    def __redraw_window(self):
        """

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.win.blit(self.win, self.win.get_rect())
        pygame.display.update()


    def run_simulation(self):
        """

        """
        for x in range(0, self.width, 1):
            for y in range(0, self.height, 1):
                rect = pygame.Rect(x*self.cell_size, y*self.cell_size, \
                                   self.cell_size, self.cell_size)
                if self.MazeObj.maze[(x,y)] == "wall":
                    pygame.draw.rect(self.win, self.BLACK, rect, 0)
                else:
                    pygame.draw.rect(self.win, self.WHITE, rect, 0)

        self.running = True
        while self.running:
            self.__redraw_window()
            


