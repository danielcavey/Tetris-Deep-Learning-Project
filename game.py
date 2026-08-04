from grid import Grid
from blocks import *
import random

# Class to govern a game
class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]                    # List of possible blocks
        self.current_block = self.get_random_block()                                                            
        self.next_block = self.get_random_block()

    # Method to randomly select a block
    def get_random_block(self):

        # Tetris rule: each block has to appear once before any one can be repeated
        # If statement governs that if all the blocks have recently appeared then the list should be refreshed
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block = random.choice(self.blocks)                                                                      # Randomly select a block
        self.blocks.remove(block)                                                                               # Remove the selected block from the list of due blocks                                                   
        return block

    # Method to move block to left
    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside() == False:                    # If the movement to the left took us outside the grid, then undo that movement
            self.current_block.move(0,1)

    # Method to move block to right
    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside() == False:                    # If the movement to the right took us outside the grid, then undo that movement
            self.current_block.move(0,-1)

    # Method to move block to down
    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside() == False:                    # If the movement down took us outside the grid, then undo that movement
            self.current_block.move(-1,0)

    # Method that uses the is_inside method to check if a tetromino is entirely within the grid
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()     # Get cell positions

        # check whether each cell is inside the grid
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    # Method to draw both the grid and the blocks on the screen
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)