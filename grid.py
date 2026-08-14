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

    # Method to check if a row is full
    def is_row_full(self,row):
        for column in range(self.num_cols):                 # for loop to check whether there is a cell in the row that is empty
            if self.grid[row][column] == 0:
                return False
        return True                                         # If empty cell not found, then return True

    # Method to clear a row
    def clear_row(self, row):
        for column in range(self.num_cols):                 # for loop to iterate through all cells in the row, and set stored value to 0
            self.grid[row][column] = 0

    # Method to move a non-empty row downwards after another row has been clear
    # Parameter row: the index of the row being looked at           (remember (0,0) is top left with row index increasing with downward movement)
    # Parameter num_rows: how many rows we want to move the current row down by (will ultimately depend on the number of lines cleared)
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):                                 # Action to be repeated for every cell in the row
            self.grid[row+num_rows][column] = self.grid[row][column]        # Move row down by the required amount num_rows
            self.grid[row][column] = 0                                      # Clear the old position

    # Method compiling the previous three functions to add functionality of clearing within game
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1,0,-1):                 # Iterate through rows in reverse order. (from self.num_rows-1 to 0 in increments of -1)
            if self.is_row_full(row):                           # If row needs cleared
                self.clear_row(row)
                completed +=1
            elif completed >0:                                  # If row doesn't need cleared but it will drop down due to previously cleared row
                self.move_row_down(row, completed)
        return completed

    # Method to reset the grid after a game over
    def reset(self):
        # Embedded for loops to iterate over every square in the grid by row and column
        for row in range(self.num_rows):                        
            for column in range(self.num_cols):
                self.grid[row][column]=0                    # Set square to be 0

    # Method to colour cells on screen according to game state
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size+11,        # x coordinate of rectangle top left. Offset by 1 to have grid lines
                                        row*self.cell_size+11,           # y coordinate of rectangle top left. Offset by 1 to have grid lines
                                        self.cell_size-1,               # rectangle width. Offset by 1 to have grid lines
                                        self.cell_size-1                # rectangle height. Offset by 1 to have grid lines
                                        )
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)            #self.colors[cell_value] selects the appropriate colour from the list in colours.py