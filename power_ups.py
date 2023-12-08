# Import necessary libraries
import pygame
import random
from abc import ABC, abstractmethod


# Define an abstract class PowerUps that inherits from ABC and pygame.sprite.Sprite
class PowerUps(ABC, pygame.sprite.Sprite):
    """
    Abstract class for power ups in the game.

    Arguments
    _________
    image_path : str, default='path_to_image.png'
        The path to the image file.
    width : int, default= 40
        The width of the power up image.
    height : int, default= 60
        The height of the power up image.
    speed : int, default= 20
        The speed of the power up movement.

    Methods
    _______
    move_forward : speed, default= 5
        Move the car forward based on the given speed.
    affect_player : player, default='player_car'
        Abstract method to affect a single player.
    affect_traffic : cars, default= 'all_coming_car_list'
        Abstract method to affect a group of cars (traffic).
    """

    # Constructor for PowerUps class that initializes common attributes for power ups
    def __init__(self, image_path, width, height, speed):
        super().__init__()
        # Load an original image and scale it to the specified width and height
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (width, height))
        # Get the rectangular area of the image
        self.rect = self.image.get_rect()
        # Store the path to the image
        self.image_path = image_path
        # Speed attribute
        self.speed = speed

    # Define method to move the power up forward based on speed
    def move_forward(self, speed):
        """
        Move the power up forward based on the given speed.

        Parameters
        __________
        speed: int
            The speed at which the power up should move
        """

        self.rect.y += self.speed * speed / 20

    # Define an abstract method that affects a single player
    @abstractmethod
    def affect_player(player):
        """
        Abstract method to affect a single player.

        Parameters
        __________
        player: str
            The player object to be affected.
        """
        pass

    # Define an abstract method that affects a group of players (traffic)
    @abstractmethod
    def affect_traffic(cars):
        """
        Abstract method to affect a group of cars (traffic).

        Parameters
        __________
        cars: str
            The group of cars to be affected.
        """
        pass


# Define an invincibility class, inheriting from PowerUps
class Invincibility(PowerUps):
    """
    Class for invincibility power up in the game.

    Arguments
    _________
    image_path : str, default='path_to_image.png'
        The path to the image file.
    width : int, default= 40
        The width of the power up image.
    height : int, default= 60
        The height of the power up image.
    speed : int, default= 20
        The speed of the power up movement.

    Methods
    _______
    move_forward : speed, default= 5
        Move the car forward based on the given speed.
    affect_player : player, default='player_car'
        Abstract method to affect a single player.
    affect_traffic : cars, default= 'all_coming_car_list'
        Abstract method to affect a group of cars (traffic).
    """

    # Constructor for the Invincibility class
    def __init__(self, image_path, width, height, speed):
        super().__init__(image_path, width, height, speed)

    # Implement the abstract method that affects a single player
    def affect_player(player):
        """
        Affect a single player with invincibility.

        Parameters
        __________
        player: str
            The player object to be affected.
        """

        # Change the player's image to the invincibility car icon
        player.original_image = pygame.image.load('images/cars/invincibility.png').convert_alpha()
        player.image = pygame.transform.scale(player.original_image, (60, 100))

    # Implement the abstract method that affects a group of players (traffic)
    def affect_traffic(cars):
        """
        Affect a group of cars (traffic) with invincibility.

        Parameters
        __________
        cars: str
            The group of cars to be affected.
        """
        # Implement logic for affecting traffic (if needed)
        pass


# Define a slowing class, inheriting from PowerUps
class Slowing(PowerUps):
    """
    Class for slowing power up in the game.

    Arguments
    _________
    image_path : str, default= 'path_to_image.png'
        The path to the image file.
    width : int, default= 40
        The width of the power up image.
    height : int, default= 60
        The height of the power up image.
    speed : int, default= 20
        The speed of the power up movement.

    Methods
    _______
    move_forward : speed, default= 5
        Move the car forward based on the given speed.
    affect_player : player, default='player_car'
        Abstract method to affect a single player.
    affect_traffic : cars, default= 'all_coming_car_list'
        Abstract method to affect a group of cars (traffic).
    """

    # Constructor for the Slowing class
    def __init__(self, image_path, width, height, speed):
        super().__init__(image_path, width, height, speed)

    # Implement the abstract method that affects a single player
    def affect_player(player):
        """
        Affect a single player with slowing.

        Parameters
        __________
        player: str
            The player object to be affected.
        """

        # Change the player's image to the slowing car icon
        player.original_image = pygame.image.load('images/cars/slow.png').convert_alpha()
        player.image = pygame.transform.scale(player.original_image, (60, 100))

    # Implement the abstract method that affects a group of players (traffic)
    def affect_traffic(cars):
        """
        Affect a group of cars (traffic) with slowing.

        Parameters
        __________
        cars: str
            The group of cars to be affected.
        """

        # Check if cars is iterable
        if hasattr(cars, '__iter__'):
            # Change the speed of each car in the all cars group to a random value
            for car in cars:
                car.change_speed(random.randint(10, 20))


# Define a small class, inheriting from PowerUps
class Small(PowerUps):
    """
    Class for small power up in the game.

    Arguments
    _________
    image_path : str, default='path_to_image.png'
        The path to the image file.
    width : int, default= 40
        The width of the power up image.
    height : int, default= 60
        The height of the power up image.
    speed : int, default= 20
        The speed of the power up movement.

    Methods
    _______
    move_forward : speed, default= 5
        Move the car forward based on the given speed.
    affect_player : player, default='player_car'
        Abstract method to affect a single player.
    affect_traffic : cars, default= 'all_coming_car_list'
        Abstract method to affect a group of cars (traffic).
    """

    # Constructor for the Small class
    def __init__(self, image_path, width, height, speed):
        super().__init__(image_path, width, height, speed)

    # Implement the abstract method that affects a single player
    def affect_player(player):
        """
        Affect a single player with size reduction.

        Parameters
        __________
        player: str
            The player object to be affected.
        """

        # Change the player's image to the small car icon and resize the car
        player.original_image = pygame.image.load('images/cars/small_car.png').convert_alpha()
        player.image = pygame.transform.scale(player.original_image, (60, 100))
        player.resize(25, 40)

    # Implement the abstract method that affects a group of players (traffic)
    def affect_traffic(cars):
        """
        Affect a group of cars (traffic) with size reduction (if needed).

        Parameters
        __________
        cars: str
            The group of cars to be affected.
        """

        pass


# Define a Speeding class, inheriting from PowerUps
class Speeding(PowerUps):
    """
    Class for speeding power up in the game.

    Arguments
    _________
    image_path : str, default='path_to_image.png'
        The path to the image file.
    width : int, default= 40
        The width of the power up image.
    height : int, default= 60
        The height of the power up image.
    speed : int, default= 20
        The speed of the power up movement.

    Methods
    _______
    move_forward : speed, default= 5
        Move the car forward based on the given speed.
    affect_player : player, default='player_car'
        Abstract method to affect a single player.
    affect_traffic : cars, default= 'all_coming_car_list'
        Abstract method to affect a group of cars (traffic).
    """

    # Constructor for the Slowing class
    def __init__(self, image_path, width, height, speed):
        super().__init__(image_path, width, height, speed)

    # Implement the abstract method that affects a single player
    def affect_player(player):
        """
        Affect a single player with increasing speed.

        Parameters
        __________
        player: str
            The player object to be affected.
        """

        # Change the player's image to the slowing car icon
        player.original_image = pygame.image.load('images/cars/fast.png').convert_alpha()
        player.image = pygame.transform.scale(player.original_image, (60, 100))

    # Implement the abstract method that affects a group of players (traffic)
    def affect_traffic(cars):
        """
        Affect a group of cars (traffic) with increasing speed.

        Parameters
        __________
        cars: str
            The group of cars to be affected.
        """

        # Check if cars is iterable
        if hasattr(cars, '__iter__'):
            # Change the speed of each car in the all cars group to a random value
            for car in cars:
                car.change_speed(random.randint(100, 150))
