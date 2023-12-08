# Import necessary library
import pygame
# Import the multi_game function from the multiplayer_game module
from multiplayer_game import multi_game


# Creating some colors using RGB scale
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
gray = (220, 220, 220)
red = (255, 0, 0)


# Creating a function that creates the winning interface
def winning_interface(player1_wins):
    """
    Display the winning interface with the outcome of the game

    Parameters
    __________
    player1_wins: bool
        True if Player 1 wins, False otherwise.
    """

    # Initiating pygame
    pygame.init()

    # Saving the screen sizes
    screenwidth = 800
    screenheight = 600
    # Creating the screen 800x600 pixels
    size = (screenwidth, screenheight)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Winning Interface")

    # Load a background image and scale it to the specified screen width and height
    background = pygame.image.load('images/background/game_over.png')
    background = pygame.transform.scale(background, (screenwidth, screenheight))

    # Load font and create some text labels
    corbel_font = pygame.font.SysFont('Corbel', 50)

    # Check if player 1 wins and display that information or otherwise
    if player1_wins:
        text = corbel_font.render("Player 1 Wins!", True, white)
    else:
        text = corbel_font.render("Player 2 Wins!", True, white)

    # Load a try again and a back image and scale them to the specified width and height
    try_again_image = pygame.image.load('images/games/try_again.png')
    try_again_image = pygame.transform.scale(try_again_image, (200, 50))
    back_image = pygame.image.load('images/games/back.png')
    back_image = pygame.transform.scale(back_image, (200, 50))

    # Set an endless loop
    carry_on = True

    # Create a clock objet with a pygame built-in function that controls the frame rate of the game
    clock = pygame.time.Clock()

    # Lost interface loop
    while carry_on:

        # Get the mouse position
        mouse = pygame.mouse.get_pos()
        # Get the input of the user
        for event in pygame.event.get():
            # Press on the exit button
            if event.type == pygame.QUIT:
                pygame.quit()
                carry_on = False
            # Detect the pressing of the button
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Press on the interface button
                if back_image.get_rect(topleft=(310, 430)).collidepoint(mouse):
                    from interface import interface
                    interface()
                # Press on the single player game button
                if try_again_image.get_rect(topleft=(310, 360)).collidepoint(mouse):
                    multi_game()

        # Setting the background image
        screen.blit(background, (0, 0))

        # Display winning message
        screen.blit(text, (300, 140))

        # Display try again image
        screen.blit(try_again_image, (310, 360))
        # Display back image
        screen.blit(back_image, (310, 430))

        # Pygame built-in function that refresh the screen
        pygame.display.flip()

        # Number of frames per second
        clock.tick(60)

    # Quit pygame
    pygame.quit()
