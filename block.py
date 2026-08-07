from colours import Colours
from position import Position
import pygame

# Parent class to define attributes and functions for a block
# Each type of block will be a child class inheriting from here

class Block:
    def __init__(self, id):
        self.id = id                                                    # Id will be used to identify the type of tetromino and therefore index colour
        self.cells = {}                                                 # Default to empty but will be defined for each tetromino child class
        self.cell_size = 30
        self.row_offset = 0                                             # Attribute that will be used to govern movement from top left corner up and down
        self.column_offset = 0                                          # Attribute that will be used to govern movement from top left corner left and right
        self.rotation_state = 0                                         # Default rotation state
        self.colours = Colours.get_cell_colours()                       # Obtain list of colours from colours.py

    # Method through which offset attributes are changed to control movement
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    # Method through which filled cells from a tile are idenfied froms rotation_state and offset attributes
    def get_cell_positions(self):
        # Identify coloured cells after rotation in default position
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            # Offset each coloured cell
            position = Position(position.row + self.row_offset,                 
                                position.column + self.column_offset
                                )               
            moved_tiles.append(position)
        return moved_tiles

    # Method to rotate a block
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):                  # If loop to check if a full rotation has been completed and if counter should be cycled back to the start
            self.rotation_state = 0

    # Method to unrotate a block
    # Will be used if a rotation takes a block into an illegal position
    def undo_rotation(self):
        self.rotation_state -=1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells)-1

    # Method to colour cells according to the tetromino
    def draw(self, screen):
        tiles = self.get_cell_positions()                             #Identify relevant cells for each tetromino block
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size+1,
                                    tile.row * self.cell_size+1,
                                    self.cell_size-1,
                                    self.cell_size-1
                                    )
            pygame.draw.rect(screen, self.colours[self.id], tile_rect)
