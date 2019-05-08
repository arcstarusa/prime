# The add function adds a new entry into the
# birthdays dictionary. 9-2
def add(birthdays):
    # Get a name and birthday.
    name = input('Enter a name: ')
    bday = input('Enter a birthday: ')

    # If the name does not exist, add it.
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('That entry already exists.')