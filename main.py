import pygame, sys
from grid import Grid
from blocks import *

pygame.init()
dark_blue = (44,44,127)                             # rgb for background

screen = pygame.display.set_mode((300,600))         # Set number of pixels in the display 
pygame.display.set_caption("Python Tetris")         # Header for the window

clock = pygame.time.Clock()

game_grid = Grid()

block = ZBlock()
block.rotation_state = 3

# Initiates game loop
while True: 
    for event in pygame.event.get():                # Cycle through all the events that have occurred
        if event.type == pygame.QUIT:               # Check if the event is to exit the application
            pygame.quit()
            sys.exit()

    screen.fill(dark_blue)                          #Set screen background color
    game_grid.draw(screen)
    block.draw(screen) 

    pygame.display.update()                         # Update display after all the events that have occurred have been resolved
    clock.tick(60)                                  # The while loop will run 60 times/second. i.e the frame rate