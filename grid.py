import pygame
from colours import Colours

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colours.get_cell_colours()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size+1,        # x coordinate of rectangle top left
                                        row*self.cell_size+1,           # y coordinate of rectangle top left
                                        self.cell_size-1,               # rectangle width
                                        self.cell_size-1                # rectangle height
                                        )
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)