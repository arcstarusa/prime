# Create a global variable. 5-15
number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print('The number you have entered is', number)

# Call the main function.
main()