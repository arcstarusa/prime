# The change function changes an existing.
# entry in the birthdays dictionary.9-2
def change(birthdays):
    # Get a name to look up.
    name = input('Enter a name: ')
    if name in birthdays:
        # Get a new birthday.
        bday = input('Enter the new birthday.')

        # Update the entry.
        birthdays[name] = bday
    else:
        print('That name is not found.')