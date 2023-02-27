import pygame
import os
import time
import sys

class Graphics():
    def __init__(self, width = 800, height = 800):
        pygame.init()

        # Define colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        
        # Define properties of the 2D array
        self.width = 800
        self.height = 800
        self.margin = 5 # Margin between each cell

        # Define properties of the window
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Line Test')
        self.win.fill(self.BLACK)
        while True:

            pygame.display.update()
        #pygame.display.update()


    def redraw_window(self):
        self.win.blit(self.image, (0, 0))
        # Update the window here
        pygame.display.update()
    
    def live(self):
        run = True
        while run:
            run = False

