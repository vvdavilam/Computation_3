# Import the interface function from the interface module
from interface import interface


# Define the main function
def main():
    """
    The main function to start the program by calling the interface function.
    """

    # Call the interface function
    interface()


# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':

    # Call the main function when the script is run directly
    main()
