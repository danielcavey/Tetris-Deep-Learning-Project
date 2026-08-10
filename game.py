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
        if self.block_inside() == False or self.block_fits() == False:   # If the movement to the left took us outside the grid or hits another block, then undo that movement
            self.current_block.move(0,1)

    # Method to move block to right
    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside() == False  or self.block_fits() == False:   # If the movement to the right took us outside the grid or hits another block, then undo that movement:                    # If the movement to the right took us outside the grid, then undo that movement
            self.current_block.move(0,-1)

    # Method to move block to down
    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside() == False or self.block_fits() == False:     # If the movement down took us outside the grid or onto another block, then undo that movement
            self.current_block.move(-1,0)
            self.lock_block()                               # Lock the block in place since it hit the bottom of the screen

    # Method to lock block in place
    # Works by 1.) updating underlying grid values; 2.) relinguishing control of current block, passing it on to new block, and creating a new "next block"
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id                   # Update grid values where current block lives
        self.current_block = self.next_block                                                        # Change current block to next block
        self.next_block = self.get_random_block()                                                   # Change next block to a random choice
        self.grid.clear_full_rows()                                                                 # Handle any rows that have completed by block locking into place

    # Method to check if a block fits
    # Does this by running is_empty() method for every tile of the block
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    # Method to rotate block
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:     # If the rotation talks the block outside the grid or onto another block, then undo that rotation
            self.current_block.undo_rotation()

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