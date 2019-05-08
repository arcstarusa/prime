# This program demonstrates passing two springs as
# keywords arguments to a function. 5-12
def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name revered is')
    reverse_name(last=last_name, first=first_name)
def reverse_name(first,last):
    print(last,first)

# Call the main function.
main()