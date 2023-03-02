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
    def __init__(self, win_width = 800, win_height = 800, width = 15, height = 15):
        """


        """

        # Define colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        
        # Define properties of the 2D array
        #self.win_width = win_width
        #self.win_height = win_height
        self.win_width = 50*width
        self.win_height = 50*height
        self.width = width
        self.height = height
        self.margin = 5 # Margin between each cell

        # Define properties of the window
        pygame.init()
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        pygame.display.set_caption('Line Test')

        # Define the maze object
        self.maze = MazeGen()


        # Testing
        for x in range(0, self.width, 2):
            for y in range(0, self.width, 2):
                pygame.draw.rect(self.win, self.WHITE, (x*50, y*50, 50, 50))

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



