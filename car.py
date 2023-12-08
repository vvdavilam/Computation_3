# Import necessary library
import pygame


# Creating some colors using RGB scale
white = (255, 255, 255)


# This class represents a car. It derives from the "Sprite" class in Pygame.
class Car(pygame.sprite.Sprite):
    """
    This is a class to create a car in a Pygame environment.

    Arguments
    _________
    original_image : pygame.Surface, default=None
        The original image of the car.
    image : pygame.Surface, default=None
        The scaled image of the car.
    speed : int, default= 0
        The speed of the car.
    rect : pygame.Rect, default=None
        The rectangular bounding box of the car.

    Attributes
    __________

    Methods
    _______
    move_right : pixels,
        Move the car to the right by the specified number of pixels.
    move_left : pixels, default=
        Move the car to the left by the specified number of pixels.
    move_up : pixels,
        Move the car upward by the specified number of pixels.
    move_down : pixels,
        Move the car downward by the specified number of pixels.
    move_forward : speed,
        Move the car forward based on the given speed.
    change_speed : speed,
        Change the speed of the car.
    repaint : new_image_path,
        Repaint the car with a new image.
    resize : width, height, 
        Resize the car's image while maintaining its position.
    """
    def __init__(self, image_path, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.speed = speed

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def move_right(self, pixels):
        """
        Move the car to the right by the specified number of pixels.

        Parameters
        __________
        pixels: int
            Number of pixels to move to the right.
        """
        self.rect.x += pixels

    def move_left(self, pixels):
        """
        Move the car to the left by the specified number of pixels.

        Parameters
        __________
        pixels: int
            Number of pixels to move to the left.
        """
        self.rect.x -= pixels

    def move_up(self, pixels):
        """
        Move the car upward by the specified number of pixels.

        Parameters
        __________
        pixels: int
            Number of pixels to move upward.
        """
        self.rect.y -= pixels

    def move_down(self, pixels):
        """
        Move the car downward by the specified number of pixels.

        Parameters
        __________
        pixels: int
            Number of pixels to move downward.
        """
        self.rect.y += pixels

    def move_forward(self, speed):
        """
        Move the car forward based on the given speed.

        Parameters
        __________
        speed: int
            The speed multiplier for moving forward.
        """
        self.rect.y += self.speed * speed / 20

    def change_speed(self, speed):
        """
        Change the speed of the car.

        Parameters
        __________
        speed: int
            The new speed value.
        """
        self.speed = speed

    def repaint(self, new_image_path):
        """
        Repaint the car with a new image.

        Parameters
        __________
        new_image_path: str
            The file path of the new image
        """
        self.original_image = pygame.image.load(new_image_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (self.rect.width, self.rect.height))

    def resize(self, width, height):
        """
        Resize the car's image while maintaining its position.

        Parameters
        __________
        width: int
            The new width of the car.
        height: int
            The new height of the car.
        """
        # Get the actual position of the player
        current_x, current_y = self.rect.x, self.rect.y

        # Resize player's image
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()

        # Adjust player's position to keep it on the same place
        self.rect.x, self.rect.y = current_x, current_y
