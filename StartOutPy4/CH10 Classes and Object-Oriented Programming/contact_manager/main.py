# This program manages contacts.
import contact
import pickle
# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the filename
FILENAME = 'contacts.dat'

# main function
def main():
    # Load the existing contact dictionary and assign it to mycontacts.
    mycontacts = load_contacts()

    # Initialize a variable for the user's choice.
    choice = 0
    # Process menu selections until the user want to quit the program.
    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()
        # Process the choice.
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
    # Save the mycontacts dictionary to a file.
    save_contacts(mycontacts)