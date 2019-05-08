# This program demonstrates the in operator
# used with a list. 7-2
def main():
    # Creeate a list of product numbers.
    prod_nums = ['V475', 'F987', 'Q143', 'R688']

    # Get a product number to search for.
    search = input ( 'Enter a product number: ')

    # Determine wheter the product number is in the list.
    if search in prod_nums:
        print(search, 'was found in the list.')
    else:
        print(search, 'was not found in the list.')

# Call the main function,
main()