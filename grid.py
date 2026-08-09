import pygame
from colours import Colours

class Grid:
    def __init__(self):
        self.num_rows = 20                                                                      # Number of rows in the tetris grid
        self.num_cols = 10                                                                      # Number of columns in the tetris grid
        self.cell_size = 30                                                                     # Number of pixels wide the square cell in the tetris grid will be
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colours.get_cell_colours()                                                # Obtain list of colours from colours.py

    # Method to print the grid in the terminal
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    # Method to determine if an arbitraty point (row, column) is inside the grid
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >=0 and column < self.num_cols:
            return True
        return False

    # Method to check in a cell is free
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    # Method to colour cells on screen according to game state
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size+1,        # x coordinate of rectangle top left. Offset by 1 to have grid lines
                                        row*self.cell_size+1,           # y coordinate of rectangle top left. Offset by 1 to have grid lines
                                        self.cell_size-1,               # rectangle width. Offset by 1 to have grid lines
                                        self.cell_size-1                # rectangle height. Offset by 1 to have grid lines
                                        )
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)            #self.colors[cell_value] selects the appropriate colour from the list in colours.py