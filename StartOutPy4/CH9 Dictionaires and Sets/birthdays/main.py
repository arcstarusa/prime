# # This program uses a dictionary to keep friends'
# names and birthdays. 9-2

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# The main function
def main():
    # Create an empty dictionary.
    birthdays = {}

    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)