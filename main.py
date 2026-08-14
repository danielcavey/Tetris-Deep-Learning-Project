import pygame, sys
from game import Game
from colours import Colours

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colours.white)
next_surface = title_font.render("Next", True, Colours.white)
game_over_surface = title_font.render("GAME OVER", True, Colours.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500,620))         # Set number of pixels in the display 
pygame.display.set_caption("Python Tetris")         # Header for the window

clock = pygame.time.Clock()

# Initiate a game
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)             # Trigger the GAME_UPDATE event every 200 miliseconds

# Initiates game loop
while True: 
    for event in pygame.event.get():                # Cycle through all the events that have occurred
        if event.type == pygame.QUIT:               # Check if the event is to exit the application
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:            # Check if the event is the user pressing a key
            if game.game_over == True:              # Code to restart the game
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:          # Check if the pressed key is left arrow and not a game over
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:         # Check if the pressed key is right arrow and not a game over
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:          # Check if the pressed key is down arrow and not a game over
                game.move_down()
                game.update_score(0,1)
            if event.key == pygame.K_UP and game.game_over == False:            # Check if the pressed key is up arrow and not a game over
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:               # Check if time has passed and and not a game over
            game.move_down()                        # Tile drop without user input

    # Code to define text for the score
    # This is contained within the game loop since it is dynamic
    score_value_surface = title_font.render(str(game.score), True, Colours.white)

    screen.fill(Colours.dark_blue)                          # Set screen background color

    # .blit() stands for block image transfer
    # It copies pixel data from one image/surface onto another surface 
    # First line puts the text score from variable score_surface onto our screen.fill() background
    # Second line puts the text Next from variable next_surface onto our screen.fill() background
    screen.blit(score_surface, (365, 20, 50, 20))                           # Rectangle (x,y) of top left then width then height
    screen.blit(next_surface, (375, 180, 50, 50))                           # Rectangle (x,y) of top left then width then height

    # Display GAME OVER text using .blit() only when required
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))                           # Rectangle (x,y) of top left then width then height

    # Add the score_rect surface to the display
    pygame.draw.rect(screen, Colours.light_blue, score_rect, 0, 10)         # Parameter 10 rounds the edges
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery = score_rect.centery))    # Position score in center of score_rect
    pygame.draw.rect(screen, Colours.light_blue, next_rect, 0, 10)         # Parameter 10 rounds the edges

    game.draw(screen)                                                       # Draw the current state of the screen 

    pygame.display.update()                         # Update display after all the events that have occurred have been resolved
    clock.tick(60)                                  # The while loop will run 60 times/second. i.e the frame rate