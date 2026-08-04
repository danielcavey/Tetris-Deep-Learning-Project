from colours import Colours
import pygame

class Block:                                # Parent class
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colours = Colours.get_cell_colours()

    def draw(self, screen):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size+1,
                                    tile.row * self.cell_size+1,
                                    self.cell_size-1,
                                    self.cell_size-1
                                    )
            pygame.draw.rect(screen, self.colours[self.id], tile_rect)
