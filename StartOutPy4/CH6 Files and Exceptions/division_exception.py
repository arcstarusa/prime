# This program divides a number by another number. 6-21

def main():
    # Get two numbers.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a another number: '))

    # If num2 is not 0k, divide num1 by num2
    # and display the result.
    if num2 != 0:
        result = num1 / num2
        print(num1, 'divided bu', num2, 'is', result)
    else:
        print('Cannot divide by zero.')

# Call the main function.
main()