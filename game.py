# Import necessary libraries
import random
import pygame
# Importing the car class and all power ups classes
from car import Car
from power_ups import Invincibility, Slowing, Small, Speeding


# Create a countdown interface function
def countdown():
    """
    Displays a countdown interface before starting the race.

    This function initiates a Pygame window and displays a countdown message
    using scaled images to create a visual countdown effect.
    """

    # Initiating pygame
    pygame.init()

    # Set up Pygame window
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Countdown")

    # Create some colors using RGB scale
    black = (0, 0, 0)

    # Load countdown images and scale them
    numbers = [pygame.image.load('images/countdown/3.png'),
               pygame.image.load('images/countdown/2.png'),
               pygame.image.load('images/countdown/1.png'),
               pygame.image.load('images/countdown/go.png')]
    scaled_numbers = [pygame.transform.scale(image, (150, 150)) for image in numbers]

    # Display the countdown images using Pygame timing events
    for image in scaled_numbers:

        # Fill the screen with black color to clear the previous image
        screen.fill(black)
        # Get the rectangle of the centered image
        image_rect = image.get_rect(center=screen.get_rect().center)
        # Display the centered and smaller images on the screen
        screen.blit(image, image_rect)
        # Update the display
        pygame.display.update()
        # Assume a consistent delay of 1 second (1000 milliseconds) between each image
        pygame.time.delay(1000)


# Creating a function that creates the main car racing game
def game():
    """
    Main function to run the single player car racing game.

    This function initializes the Pygame window, sets up the game environment,
    handles game events, contains the main game loop, and continuously refreshes the screen.
    It includes logic for player car movement, collision detection, power up effects, and more.
    """

    # Call the countdown function that
    # initiates the countdown before the start of the race
    countdown()

    # Initiating pygame
    pygame.init()

    # Amount of pixels that the height and width take
    screenwidth = 800
    screenheight = 600
    # Creating the game screen 800x600 pixels
    size = (screenwidth, screenheight)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing Game")

    # Load a background image and scale it to the specified screen width and height
    background = pygame.image.load('images/background/game.png')
    background = pygame.transform.scale(background, size)

    # Load font
    comic_sans_font = pygame.font.SysFont('Comic Sans MS', 30)

    # Load the pauses images and scale them to the specified width and height
    pause_image = pygame.image.load('images/games/pause.png')
    pause_image = pygame.transform.scale(pause_image, (110, 46))
    paused_image = pygame.image.load('images/games/paused.png')
    paused_image = pygame.transform.scale(paused_image, (400, 300))
    play_image = pygame.image.load('images/games/play.png')
    play_image = pygame.transform.scale(play_image, (200, 46))
    try_again_image = pygame.image.load('images/games/try_again.png')
    try_again_image = pygame.transform.scale(try_again_image, (200, 46))
    back_image = pygame.image.load('images/games/back.png')
    back_image = pygame.transform.scale(back_image, (200, 40))

    # Create some colors using RGB scale
    white = (255, 255, 255)
    gray = (224, 224, 224)
    yellow = (255, 255, 0)

    # Function to draw a dashed line
    def draw_dashed_line(surface, color, start, end, dash_length, gap_length, width):
        """
        Function to draw a dashed line on a given surface.

        Parameters
        __________
        surface: pygame.Surface
            The surface on which to draw the dashed line.
        color: tuple
            The RGB color of the dashed line.
        start: tuple
            (x, y) coordinates of the starting point of the dashed line.
        end: tuple
            (x, y) coordinates of the ending point of the dashed line.
        dash_length: int
            Length of each dash in pixels.
        gap_length: int
            Length of each gap between dashes in pixels.
        width: int
            Width of the dashed line.
        """

        # Extract the coordinates of the starting and ending point
        x1, y1 = start
        x2, y2 = end
        # Calculate the differences in x and y coordinates
        dx = x2 - x1
        dy = y2 - y1
        # Calculate the distance between the starting and ending points
        distance = max(abs(dx), abs(dy))
        # Normalize the differences to get the unit vector (Represent the direction of the line)
        dx = dx / distance
        dy = dy / distance

        # Initialize the current position to the starting point
        x, y = x1, y1
        # Iterate through the distance, drawing dashes and gaps
        for space in range(int(distance / (dash_length + gap_length))):
            # Draw a line segment (dash) on the surface
            pygame.draw.line(
                surface,
                color,
                (round(x), round(y)),
                (round(x + dash_length * dx), round(y + dash_length * dy)),
                width
            )
            # Move the current position to the next dash position
            x += (dash_length + gap_length) * dx
            y += (dash_length + gap_length) * dy

    # Set initial speeds
    speed = 1

    # List of cars
    cars_list = ('images/cars/grey.png', 'images/cars/dark_blue.png', 'images/cars/cyan.png', 'images/cars/green.png',
                 'images/cars/white.png', 'images/cars/purple.png', 'images/cars/yellow.png', 'images/cars/blue.png',
                 'images/cars/lime.png', 'images/cars/orange.png', 'images/cars/pink.png')

    # Positions in x that the power ups can take
    x_positions = [68, 168, 268, 368]

    # Create instances for the player car, all the computer-controlled cars and all powerups
    player_car = Car('images/cars/red.png', 60, 100, 70)
    player_car.rect.x = 160
    player_car.rect.y = screenheight - 100

    car1 = Car('images/cars/yellow.png', 60, 100, random.randint(50, 100))
    car1.rect.x = 60
    car1.rect.y = 0

    car2 = Car('images/cars/purple.png', 60, 100, random.randint(50, 100))
    car2.rect.x = 160
    car2.rect.y = -200

    car3 = Car('images/cars/lime.png', 60, 100, random.randint(50, 100))
    car3.rect.x = 260
    car3.rect.y = -500

    car4 = Car('images/cars/blue.png', 60, 100, random.randint(50, 100))
    car4.rect.x = 360
    car4.rect.y = -50

    power_up1 = Invincibility('images/power_ups/shield.png', 40, 60, 40)
    power_up1.rect.x = random.choice(x_positions)
    power_up1.rect.y = -5

    power_up2 = Slowing('images/power_ups/time.png', 40, 60, 30)
    power_up2.rect.x = random.choice(x_positions)
    power_up2.rect.y = -500

    power_up3 = Small('images/power_ups/small.png', 40, 60, 25)
    power_up3.rect.x = random.choice(x_positions)
    power_up3.rect.y = -1000

    power_up4 = Speeding('images/power_ups/fast.png', 40, 60, 30)
    power_up4.rect.x = random.choice(x_positions)
    power_up4.rect.y = -1800

    # Create sprite groups for the player car, all the computer-controlled cars and all power ups
    # This is a list that will contain all the sprites we intend to use in the game.
    all_sprites_list = pygame.sprite.Group()
    all_coming_cars_list = pygame.sprite.Group()
    all_coming_power_ups = pygame.sprite.Group()

    # Add the player car, all the computer-controlled cars and all power ups to the specific lists of objects
    all_sprites_list.add(player_car, car1, car2, car3, car4, power_up1, power_up2, power_up3, power_up4)
    all_coming_cars_list.add(car1, car2, car3, car4)
    all_coming_power_ups.add(power_up1, power_up2, power_up3, power_up4)

    # Set initial power ups states
    invincible = False
    active_power = False
    slow_time = False
    speed_time = False

    # Initial power ups time and save it
    start_power = pygame.time.get_ticks()

    # Set initial game states variables
    paused = False
    show_popup = False

    # Initial game time and save it
    start_time = pygame.time.get_ticks()

    # Set an endless (main game) loop
    carry_on = True

    # Create a clock objet with a pygame built-in function that controls the frame rate of the game
    clock = pygame.time.Clock()

    # Main game loop
    while carry_on:

        # Event handling loop using pygame built-in function events
        for event in pygame.event.get():
            # Check if the quit button is pressed (if it is pressed window closes)
            if event.type == pygame.QUIT:
                carry_on = False
            # Check if mouse button is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position
                mouse_pos = pygame.mouse.get_pos()
                # Check if the mouse button click is on the paused button
                if paused_image.get_rect(topleft=(670, 10)).collidepoint(mouse_pos):
                    # Toggle the pause state and show/hide the pause popup
                    paused = not paused
                    show_popup = paused
                # Check if the game is paused
                elif show_popup:
                    # Check if the mouse button click is on the play, try again, or back button in the pause popup
                    if play_image.get_rect(topleft=(300, 270)).collidepoint(mouse_pos):
                        paused = False
                        show_popup = False
                    # Restart the game if the "Try again" button is clicked
                    elif try_again_image.get_rect(topleft=(300, 325)).collidepoint(mouse_pos):
                        game()
                    # Go back to the main interface if the "Back" button is clicked
                    elif back_image.get_rect(topleft=(300, 380)).collidepoint(mouse_pos):
                        from interface import interface
                        interface()

        # Game logic when the game is not paused
        if not paused:

            # Move player car according to keyboard input
            keys = pygame.key.get_pressed()
            # Limit movement to the left
            if keys[pygame.K_LEFT] and player_car.rect.x > 40:
                player_car.move_left(5)
            # Limit movement to the right
            if keys[pygame.K_RIGHT] and player_car.rect.x < 380:
                player_car.move_right(5)
            # Limit upward movement
            if keys[pygame.K_UP] and player_car.rect.y > 0:
                player_car.move_up(5)
            # Limit downward movement
            if keys[pygame.K_DOWN] and player_car.rect.y < screenheight - player_car.rect.height:
                player_car.move_down(5)

            # Calculate the time elapsed since the start of the game in seconds (/1000)
            time_elapsed = (pygame.time.get_ticks() - start_time) / 1000
            # Show elapsed time as score in the top right corner
            text_score = comic_sans_font.render("Score: " + str(int(time_elapsed)), True, white)

            # Game logic for all coming cars
            for car in all_coming_cars_list:

                # Move the given car forward based on the specified speed
                car.move_forward(speed)

                # Check if the car has moved off the screen
                if car.rect.y >= screenheight:
                    # Reset position, appearance, and speed of all coming cars when they go off the screen
                    car.repaint(random.choice(cars_list))
                    car.change_speed(random.randint(40, 100))
                    car.rect.y = -200

                # Check if the car is on the screen and neither slowing nor speeding power ups are active
                if car.rect.y <= screenheight and not slow_time and not speed_time:
                    # Change the car's speed to a random value within the specified range
                    car.change_speed(random.randint(40, 100))

                # Check if the car is on the screen and the slowing power up is active
                elif car.rect.y <= screenheight and slow_time:
                    # Apply the slowing effect to the car's speed
                    Slowing.affect_traffic(all_coming_cars_list)

                # Check if the car is on the screen and the speeding power up is active
                elif car.rect.y <= screenheight and speed_time:
                    # Apply the speeding effect to the car's speed
                    Speeding.affect_traffic(all_coming_cars_list)

                # Check if there is a car collision with the player car, considering the player car is not invincible
                if not invincible:
                    # Check if the player car collides with any of the computer-controlled cars
                    if pygame.sprite.collide_mask(player_car, car) is not None:
                        # Print a message indicating a car crash
                        print("Car Crash!")
                        # End of the game
                        carry_on = False

                # If there is a car collision, display the lost interface
                if not carry_on:
                    import lost_interface
                    lost_interface.lost_interface(int(time_elapsed))

                # Generate new power up when there are no power ups on the screen
                if len(all_coming_power_ups) < 1:

                    # Define the classes of power ups with their probabilities
                    power_up_classes = [Invincibility, Invincibility, Invincibility, Invincibility, Invincibility,
                                        Slowing, Slowing, Slowing, Slowing,
                                        Small, Small, Small,
                                        Speeding]

                    # Randomly choose a power up class from the defined list
                    random_power_up_class = random.choice(power_up_classes)

                    # Define image paths for each power up class
                    invincibility_image_path = 'images/power_ups/shield.png'
                    slowing_image_path = 'images/power_ups/time.png'
                    small_image_path = 'images/power_ups/small.png'
                    speed_image_path = 'images/power_ups/fast.png'

                    # Determine the image path based on the selected power up class
                    if random_power_up_class == Invincibility:
                        image_path = invincibility_image_path
                    elif random_power_up_class == Slowing:
                        image_path = slowing_image_path
                    elif random_power_up_class == Small:
                        image_path = small_image_path
                    elif random_power_up_class == Speeding:
                        image_path = speed_image_path

                    # Create a new instance of the selected power up class with random characteristics
                    new_power_up = random_power_up_class(image_path, 40, 60, random.randint(20, 100))

                    # Randomly select a position X from the list for the new power up
                    new_position_x = random.choice(x_positions)
                    # Random Y coordinate for power up
                    new_position_y = random.randint(-150, 0)

                    # Set the position of the new power up
                    new_power_up.rect.x = new_position_x
                    new_power_up.rect.y = new_position_y

                    # Add the new power up to the groups of power ups and all sprites
                    all_coming_power_ups.add(new_power_up)
                    all_sprites_list.add(new_power_up)

            # Game logic for all power ups
            for power_up in all_coming_power_ups:

                # Move the given power up forward based on the specified speed
                power_up.move_forward(speed)

                # Detect collision between the player car and power ups
                collided_power_up = pygame.sprite.collide_mask(player_car, power_up)

                # Remove the power up if it exits the screen or collides with the player car
                if power_up.rect.y > screenheight or collided_power_up:
                    power_up.kill()

                # Check if there is a collision with the player car and the power up is not already active
                if collided_power_up and not active_power:
                    # Check the type of power up and apply the corresponding effect
                    if power_up.image_path == 'images/power_ups/small.png':
                        # Apply the small power up effect to the player car
                        Small.affect_player(player_car)
                        # Print a message indicating that the small power up has been activated
                        print("Small!")
                        # Set the power up as active to prevent further collisions during its effect duration
                        active_power = True

                    elif power_up.image_path == 'images/power_ups/shield.png':
                        # Apply the invincibility power up effect to the player car
                        Invincibility.affect_player(player_car)
                        # Print a message indicating that the invincibility power up has been activated
                        print("Invincibility!")
                        # Set the invincibility state to true
                        invincible = True
                        # Set the power up as active to prevent further collisions during its effect duration
                        active_power = True

                    elif power_up.image_path == 'images/power_ups/time.png':
                        # Apply the slowing power up effect to the player car
                        # and all computer-controlled cars in the list
                        Slowing.affect_player(player_car)
                        Slowing.affect_traffic(all_coming_cars_list)
                        # Print a message indicating that the slowing power up has been activated
                        print("Slowing!")
                        # Set the slowing state to true
                        slow_time = True
                        # Set the power up as active to prevent further collisions during its effect duration
                        active_power = True

                    elif power_up.image_path == 'images/power_ups/fast.png':
                        # Apply the speeding power up effect to the player car
                        # and all computer-controlled cars in the list
                        Speeding.affect_player(player_car)
                        Speeding.affect_traffic(all_coming_cars_list)
                        # Print a message indicating that the speeding power up has been activated
                        print("Speeding!")
                        # Set the speeding state to true
                        speed_time = True
                        # Set the power up as active to prevent further collisions during its effect duration
                        active_power = True

                    # Record the time when the power up was obtained
                    start_power = pygame.time.get_ticks()

            # Check if the power up effect duration has expired (5 seconds duration)
            if ((pygame.time.get_ticks() - start_power) / 1000) > 5:
                # Reset power up states and player car image to default
                invincible = False
                active_power = False
                slow_time = False
                speed_time = False
                player_car.original_image = pygame.image.load('images/cars/red.png').convert_alpha()
                player_car.image = pygame.transform.scale(player_car.original_image, (60, 100))

        # Update all sprites
        all_sprites_list.update()

        # Drawing the screen
        screen.blit(background, (0, 0))

        # Draw the road
        pygame.draw.rect(screen, gray, [40, 0, 400, screenheight])
        # Draw the dashed lines, painting on the road
        draw_dashed_line(screen, white, [140, 0], [140, screenheight], 20, 10, 4)
        draw_dashed_line(screen, white, [240, 0], [240, screenheight], 20, 10, 4)
        draw_dashed_line(screen, white, [340, 0], [340, screenheight], 20, 10, 4)
        # Draw the lines that bound the road
        pygame.draw.line(screen, yellow, [50, 0], [50, screenheight], 3)
        pygame.draw.line(screen, yellow, [430, 0], [430, screenheight], 3)

        # Draw all the sprites on the screen
        all_sprites_list.draw(screen)

        # Show time as score
        screen.blit(text_score, (650, 60))

        # Show the pause screen
        screen.blit(pause_image, (670, 10))

        # Display the paused popup and buttons for play, try again, and back
        if show_popup:
            screen.blit(paused_image, (200, 150))
            screen.blit(play_image, (300, 268))
            screen.blit(try_again_image, (300, 325))
            screen.blit(back_image, (300, 380))

        # Pygame built-in function that refresh the screen
        pygame.display.flip()

        # Number of frames per second
        clock.tick(60)

    # Quitting pygame
    pygame.quit()
