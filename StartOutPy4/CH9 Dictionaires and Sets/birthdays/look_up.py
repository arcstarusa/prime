# The look_up funciton looks up a name in the
# birthdays dictionary. 9-2
def look_up(birthdays):
    # Get a name to look up.
    name = input('Enter a name: ')

    # Look it up in the dictionary
    print(birthdays.get(name, 'Not found.'))