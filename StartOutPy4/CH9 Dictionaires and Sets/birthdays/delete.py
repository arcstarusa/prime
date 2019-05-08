# The delete function deletes an entry from the
# birthdays dictionary.9-2
def delete(birthdays):
    # Get a name to look up.
    name = input('Enter a name: ')

    # If the name is found, delete the entry.
    if name in birthdays:
        del birthdays[name]
    else:
        print('That name is not found.')

# Call the main function
main()