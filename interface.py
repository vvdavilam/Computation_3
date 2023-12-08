"""
Main interface function to manage the game menu and screens.

This function initializes the Pygame module, sets up the game window, handles user input,
and displays the main menu, instructions screen, and credits screen.
"""

# Import necessary library
import pygame
# Import the game and multi_game function from the game and multiplayer_game module respectively
from game import game
from multiplayer_game import multi_game

# Define states for different screens
MAIN_MENU = 0
CREDITS_SCREEN = 1
INSTRUCTIONS_SCREEN = 2


# Create a main interface function
def interface():
    """
    Initialize and manage the game interface.

    This function sets up the Pygame environment, including the game window, fonts, and button images.
    It handles user input to navigate between the main menu, instructions screen, and credits screen.
    The funtion also manages the volume control and music playback.
    """

    # Initiate pygame
    pygame.init()

    # Initialize pygame mixer
    pygame.mixer.music.load('musics/interface.mp3')

    # Play music in loop indefinitely
    pygame.mixer.music.play(-1)

    # Initialize the volume
    volume = 0.5

    # Create the screen (720x720 pixels)
    size = (720, 720)
    screen = pygame.display.set_mode(size)

    # Load and scale background image
    background = pygame.image.load('images/background/interface.png').convert()
    background = pygame.transform.scale(background, size)

    # Define color constants (RBG scale)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)
    gray = (220, 220, 220)
    purple = (178, 102, 255)
    pink = (255, 0, 127)

    # Define font
    pixel_font = pygame.font.Font('fonts/pixel.ttf', 20)
    corbel_font = pygame.font.SysFont('Corbel', 20)
    arial_font = pygame.font.SysFont('Arial', 20)
    glitch_font = pygame.font.Font('fonts/glitch.ttf', 40)

    # Load and scale button images
    start_button_image = pygame.image.load("images/interface/start_button.png")
    game1_text = pygame.transform.scale(start_button_image, (160, 70))
    multiplayer_button_image = pygame.image.load("images/interface/Multiplayer.png")
    game2_text = pygame.transform.scale(multiplayer_button_image, (165, 75))
    instructions_button_image = pygame.image.load("images/interface/instructions.png")
    game3_text = pygame.transform.scale(instructions_button_image, (160, 50))
    credits_button_image = pygame.image.load("images/interface/credits.png")
    credits_text = pygame.transform.scale(credits_button_image, (100, 40))
    quit_button_image = pygame.image.load("images/interface/quit.png")
    quit_text = pygame.transform.scale(quit_button_image, (100, 40))

    # Define the rounded rectangle drawing function outside the main loop
    def draw_rounded_rect_with_image(screen, image, rect, color, border_radius):
        """
        Draw a rounded rectangle with an image centered inside it.

        Parameters
        __________
        screen: pygame.Surface
            The game window surface.
        image: pygame.Surface
            The image to be displayed on the button.
        rect: list
            The rectangle coordinates [x, y, width, height] of the button.
        color: tuple
            The RGB color of the button
        border_radius: int
            The radius of the rounded corners.
        """
        pygame.draw.rect(screen, color, rect, border_radius=border_radius)
        screen.blit(image, (rect[0] + (rect[2] - image.get_width()) // 2,
                            rect[1] + (rect[3] - image.get_height()) // 2))

    # Set the initial state
    current_state = MAIN_MENU

    # Interface loop
    while True:
        # Getting the mouse position
        mouse = pygame.mouse.get_pos()
        # Getting the input of the user
        for ev in pygame.event.get():
            # Press on the exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # Detect the pressing of the buttons
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse clicks
                if current_state == MAIN_MENU:
                    # Press on the single player game button
                    if 310 <= mouse[0] <= 460 and 250 <= mouse[1] <= 295:
                        game()
                    # Press on the multiplayer game button
                    elif 306 <= mouse[0] <= 466 and 320 <= mouse[1] <= 365:
                        multi_game()
                    # Redirect to the instructions screen
                    elif 306 <= mouse[0] <= 466 and 390 <= mouse[1] <= 435:
                        current_state = INSTRUCTIONS_SCREEN
                    # Redirect to the credits screen
                    elif 20 <= mouse[0] <= 165 and screen.get_height() - 80 <= mouse[1] <= screen.get_height() - 20:
                        current_state = CREDITS_SCREEN
                    # Press on the quit button
                    elif screen.get_width() - 165 <= mouse[0] <= screen.get_width() - 20 and screen.get_height() - 80\
                            <= mouse[1] <= screen.get_height() - 20:
                        pygame.quit()
                # Redirect back to the main menu
                elif current_state == INSTRUCTIONS_SCREEN:
                    if 20 <= mouse[0] <= 100 and 20 <= mouse[1] <= 60:
                        current_state = MAIN_MENU
                # Redirect back to the main menu
                elif current_state == CREDITS_SCREEN:
                    if 20 <= mouse[0] <= 100 and 20 <= mouse[1] <= 60:
                        current_state = MAIN_MENU

        # Check if keys are getting pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            # Increase volume when the up arrow key is pressed
            volume = min(1.0, volume + 0.1)
            pygame.mixer.music.set_volume(volume)
        elif keys[pygame.K_DOWN]:
            # Decrease volume when the down arrow key is pressed
            volume = max(0.0, volume - 0.1)
            pygame.mixer.music.set_volume(volume)
        elif keys[pygame.K_SPACE]:
            # Stop music when the space key is pressed
            pygame.mixer.music.stop()

        # Set the background image
        screen.blit(background, (0, 0))

        # Render text for controls
        volume_text = arial_font.render(f"Volume: {int(volume * 100)}%", True, white)
        screen.blit(volume_text, (10, 10))

        # Render main menu buttons
        if current_state == MAIN_MENU:
            draw_rounded_rect_with_image(screen, game1_text, [310, 250, 150, 45],
                                         green if 310 <= mouse[0] <= 450 and 250 <= mouse[1] <= 295 else gray, 15)

            draw_rounded_rect_with_image(screen, game2_text, [306, 320, 160, 45],
                                         purple if 306 <= mouse[0] <= 466 and 320 <= mouse[1] <= 365 else gray, 15)

            draw_rounded_rect_with_image(screen, game3_text, [306, 390, 160, 45],
                                         pink if 306 <= mouse[0] <= 466 and 390 <= mouse[1] <= 435 else gray, 15)

            draw_rounded_rect_with_image(screen, credits_text, [20, screen.get_height() - 80, 100, 40],
                                         yellow if 20 <= mouse[0] <= 120 and screen.get_height() - 80
                                                    <= mouse[1] <= screen.get_height() - 40 else gray, 15)
            draw_rounded_rect_with_image(screen, quit_text,
                                         [screen.get_width() - 120, screen.get_height() - 80, 100, 40],
                                         red if screen.get_width() - 120 <= mouse[
                                             0] <= screen.get_width() - 20 and screen.get_height() - 80 <= mouse[
                                                    1] <= screen.get_height() - 40 else gray, 15)

        # Render credits screen
        elif current_state == CREDITS_SCREEN:
            # Load a background image and scale it to the specified screen's size
            background_credits = pygame.image.load('images/background/credits_background.png').convert()
            background_credits = pygame.transform.scale(background_credits, (screen.get_width(), screen.get_height()))
            screen.blit(background_credits, (0, 0))

            # Create text labels
            credits_1 = arial_font.render("Margarida Ourives 20221809", True, white)
            screen.blit(credits_1, (255, 160))
            credits_2 = arial_font.render("Nayma Assis 20221965", True, white)
            screen.blit(credits_2, (275, 190))
            credits_3 = arial_font.render("Veronica Mendes 20221945", True, white)
            screen.blit(credits_3, (255, 220))
            credits_4 = arial_font.render("Supported by:", True, white)
            screen.blit(credits_4, (310, 250))
            credits_5 = arial_font.render("Professor João Fonseca", True, white)
            screen.blit(credits_5, (268, 280))
            credits_6 = arial_font.render("Professor Liah Rosenfeld", True, white)
            screen.blit(credits_6, (265, 310))
            credits_7 = arial_font.render("Professor Davide Farinati", True, white)
            screen.blit(credits_7, (265, 340))

            # Draw a rounded back button
            button_color = white
            button_rect = pygame.Rect(10, 10, 70, 30)
            pygame.draw.rect(screen, button_color, button_rect, border_radius=15)
            back_text = pixel_font.render('Back', True, pink)

            # Center the text within the button
            text_rect = back_text.get_rect()
            text_rect.center = button_rect.center

            # Blit the text at the specified rectangle coordinates
            screen.blit(back_text, text_rect)

        # Render instructions screen
        elif current_state == INSTRUCTIONS_SCREEN:
            # Load a background image and scale it to the specified screen's size
            background_instructions = pygame.image.load('images/background/instructions_background.png').convert()
            background_instructions = pygame.transform.scale(background_instructions,
                                                             (screen.get_width(), screen.get_height()))
            screen.blit(background_instructions, (0, 0))

            # Define the text for each section
            welcome_text = glitch_font.render('Welcome to Speed Rush Game instructions', True, white)
            screen.blit(welcome_text, (150, 30))

            main_objective_text = corbel_font.render("Game objective:", True, white)
            screen.blit(main_objective_text, (30, 80))
            objective_text = arial_font.render("In this game the player has to navigate "
                                              "through oncoming vehicles without colliding.", True, white)
            screen.blit(objective_text, (50, 110))

            single_multiplayer_title = corbel_font.render("Single Player & Multiplayer Options:", True, white)
            screen.blit(single_multiplayer_title, (30, 150))

            singleplayer_text = arial_font.render("-Single Player Mode: Use the arrow keys to control the car.", True,
                                                 white)
            screen.blit(singleplayer_text, (50, 180))
            multiplayer_text = arial_font.render("-Multiplayer Mode: One player uses the arrow keys "
                                                "while another uses W, A, S, D.", True, white)
            screen.blit(multiplayer_text, (50, 210))

            powerups_text = corbel_font.render("Power-ups:", True, white)
            screen.blit(powerups_text, (30, 250))
            invincibility_text = arial_font.render(
                "1. Invincibility Power-up: Provides temporary invincibility to the player.", True, white)
            screen.blit(invincibility_text, (50, 280))
            slowing_text = arial_font.render("2. Slowing Power-up: Temporarily slows down incoming traffic cars.", True,
                                            white)
            screen.blit(slowing_text, (50, 330))
            size_alteration_text = arial_font.render(
                "3. Size Alteration Power-up: Temporarily changes the size of the player's car.", True, white)
            screen.blit(size_alteration_text, (50, 380))
            speeding_text = arial_font.render("4. Speeding Power-up: Temporarily speeds up the player car.", True,
                                             white)
            screen.blit(speeding_text, (50, 430))

            # Draw a rounded back button
            button_color = white
            button_rect = pygame.Rect(10, 10, 60, 30)
            pygame.draw.rect(screen, button_color, button_rect, border_radius=15)
            button_text = arial_font.render('Back', True, black)

            # Center the text within the button
            text_rect = button_text.get_rect()
            text_rect.center = button_rect.center

            # Blit the text at the specified rectangle coordinates
            screen.blit(button_text, text_rect)

        # Pygame built-in function that updates the screen at every operation of the loop
        pygame.display.update()

    # Quit pygame mixer
    pygame.mixer.quit()
