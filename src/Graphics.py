import pygame
import os
import time
import sys

sys.path.append(str(sys.path[0][:-14]))
dirname = os.getcwd()
sys.path.insert(1, os.path.join(dirname))

from MazeGen import MazeGen

"""

"""

class Graphics():
    def __init__(self, width = 15, height = 15):
        """


        """
        # Define colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        
        # Define properties of the 2D array
        self.cell_size = 50
        self.width = width
        self.height = height
        self.win_width = self.cell_size*self.width
        self.win_height = self.cell_size*self.height
        self.margin = 5 # Margin between each cell

        # Define properties of the window
        pygame.init()
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        pygame.display.set_caption('Line Test')

        # Define the maze object
        self.maze = MazeGen()
        print(type(self.maze))

        # Testing, but iterate over the self.maze object
        for x in range(0, self.width, 2):
            for y in range(0, self.width, 2):
                pygame.draw.rect(self.win, self.WHITE, (x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size))

    def __redraw_window(self):
        """

        """
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running=0
        self.win.blit(self.win, self.win.get_rect())
        #self.win.fill(self.BLACK)
        pygame.display.flip()


    def run_simulation(self):
        """

        """
        i = 0
        while True:
            self.__redraw_window()
            i += 1
            if i > 5000:
                break



