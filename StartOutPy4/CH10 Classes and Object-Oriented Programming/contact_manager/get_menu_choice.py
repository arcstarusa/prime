# The get_menu_choice function displays the menu and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Menu')
    print('-----------------------')
    print('1. Lookup a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact.')
    print('5. Quit the program.')
    print()
    # Get the user's choice.
    choice=int(input('Enter your choice: '))
    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice
