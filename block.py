from colours import Colours
import pygame

# Parent class to define attributes and functions for a block
# Each type of block will be a child class inheriting from here

class Block:
    def __init__(self, id):
        self.id = id                                                    # Id will be used to identify the type of tetromino and therefore index colour
        self.cells = {}                                                 # Default to empty but will be defined for each tetromino child class
        self.cell_size = 30
        self.rotation_state = 0                                         # Default rotation state
        self.colours = Colours.get_cell_colours()                       # Obtain list of colours from colours.py

    # Function to colour cells according to the tetromino
    def draw(self, screen):
        tiles = self.cells[self.rotation_state]                             #Identify relevant cells for each tetromino block
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size+1,
                                    tile.row * self.cell_size+1,
                                    self.cell_size-1,
                                    self.cell_size-1
                                    )
            pygame.draw.rect(screen, self.colours[self.id], tile_rect)
