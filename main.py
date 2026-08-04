import pygame, sys
from game import Game

pygame.init()
dark_blue = (44,44,127)                             # rgb for background

screen = pygame.display.set_mode((300,600))         # Set number of pixels in the display 
pygame.display.set_caption("Python Tetris")         # Header for the window

clock = pygame.time.Clock()

# Initiate a game
game = Game()

# Initiates game loop
while True: 
    for event in pygame.event.get():                # Cycle through all the events that have occurred
        if event.type == pygame.QUIT:               # Check if the event is to exit the application
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:            # Check if the event is the user pressing a key
            if event.key == pygame.K_LEFT:          # Check if the pressed key is left arrow
                game.move_left()
            if event.key == pygame.K_RIGHT:         # Check if the pressed key is right arrow
                game.move_right()
            if event.key == pygame.K_DOWN:         # Check if the pressed key is down arrow
                game.move_down()

    screen.fill(dark_blue)                          #Set screen background color
    game.draw(screen)

    pygame.display.update()                         # Update display after all the events that have occurred have been resolved
    clock.tick(60)                                  # The while loop will run 60 times/second. i.e the frame rate