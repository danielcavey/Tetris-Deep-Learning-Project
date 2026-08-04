from block import Block
from position import Position

# Different child class for each tetromino type inhertiting from parent class Block

# Child class for L-shaped block
class LBlock(Block):
    def __init__(self):
        super().__init__(id=1)
        self.cells = {
            0: [Position(0,2), Position(1,0), Position(1,1), Position(1,2)],                # Cells that would be occupied by tile under default rotation
            1: [Position(0,1), Position(1,1), Position(2,1), Position(2,2)],                # Cells that would be occupied by tile under 90 degree roation clockwise
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,0)],                # Cells that would be occupied by tile under 180 degree roation clockwise
            3: [Position(0,0), Position(0,1), Position(1,1), Position(2,1)]                 # Cells that would be occupied by tile under 270 degree roation clockwise
        }
        self.move(0,3)                  # Move tetromino to default start in the middle of the top row

# Child class for J-shaped block
class JBlock(Block):
    def __init__(self):
        super().__init__(id=2)
        self.cells = {
            0: [Position(0,0), Position(1,0), Position(1,1), Position(1,2)],                # Cells that would be occupied by tile under default rotation
            1: [Position(0,1), Position(0,2), Position(1,1), Position(2,1)],                # Cells that would be occupied by tile under 90 degree roation clockwise
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,2)],                # Cells that would be occupied by tile under 180 degree roation clockwise
            3: [Position(0,1), Position(1,1), Position(2,0), Position(2,1)]                 # Cells that would be occupied by tile under 270 degree roation clockwise
        }
        self.move(0,3)                  # Move tetromino to default start in the middle of the top row

# Child class for I-shaped block
class IBlock(Block):
    def __init__(self):
        super().__init__(id=3)
        self.cells = {
            0: [Position(1,0), Position(1,1), Position(1,2), Position(1,3)],                # Cells that would be occupied by tile under default rotation
            1: [Position(0,2), Position(1,2), Position(2,2), Position(3,2)],                # Cells that would be occupied by tile under 90 degree roation clockwise
            2: [Position(2,0), Position(2,1), Position(2,2), Position(2,3)],                # Cells that would be occupied by tile under 180 degree roation clockwise
            3: [Position(0,1), Position(1,1), Position(2,1), Position(3,1)]                 # Cells that would be occupied by tile under 270 degree roation clockwise
        }
        self.move(-1,3)                 # Move tetromino to default start in the middle of the top row. Note I-block has to be shifted up one additional space

# Child class for O-shaped block
class OBlock(Block):
    def __init__(self):
        super().__init__(id=4)
        self.cells = {
            0: [Position(0,0), Position(1,0), Position(0,1), Position(1,1)]                 # Cells that would be occupied by tile. No impact of rotation here.
        }
        self.move(0,4)                  # Move tetromino to default start in the middle of the top row. Note O-block has to be shifted right one additional space

# Child class for S-shaped block
class SBlock(Block):
    def __init__(self):
        super().__init__(id=5)
        self.cells = {
            0: [Position(0,1), Position(0,2), Position(1,0), Position(1,1)],                # Cells that would be occupied by tile under default rotation
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,2)],                # Cells that would be occupied by tile under 90 degree roation clockwise
            2: [Position(1,1), Position(1,2), Position(2,0), Position(2,1)],                # Cells that would be occupied by tile under 180 degree roation clockwise
            3: [Position(0,0), Position(1,0), Position(1,1), Position(2,1)]                 # Cells that would be occupied by tile under 270 degree roation clockwise
        }
        self.move(0,3)                  # Move tetromino to default start in the middle of the top row

# Child class for T-shaped block
class TBlock(Block):
    def __init__(self):
        super().__init__(id=6)
        self.cells = {
            0: [Position(0,1), Position(1,0), Position(1,1), Position(1,2)],                # Cells that would be occupied by tile under default rotation
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,1)],                # Cells that would be occupied by tile under 90 degree roation clockwise
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,1)],                # Cells that would be occupied by tile under 180 degree roation clockwise
            3: [Position(0,1), Position(1,0), Position(1,1), Position(2,1)]                 # Cells that would be occupied by tile under 270 degree roation clockwise
        }
        self.move(0,3)                  # Move tetromino to default start in the middle of the top row

# Child class for Z-shaped block
class ZBlock(Block):
    def __init__(self):
        super().__init__(id=7)
        self.cells = {
            0: [Position(0,0), Position(0,1), Position(1,1), Position(1,2)],                # Cells that would be occupied by tile under default rotation
            1: [Position(0,2), Position(1,1), Position(1,2), Position(2,1)],                # Cells that would be occupied by tile under 90 degree roation clockwise
            2: [Position(1,0), Position(1,1), Position(2,1), Position(2,2)],                # Cells that would be occupied by tile under 180 degree roation clockwise
            3: [Position(0,1), Position(1,0), Position(1,1), Position(2,0)]                 # Cells that would be occupied by tile under 270 degree roation clockwise
        }
        self.move(0,3)                  # Move tetromino to default start in the middle of the top row