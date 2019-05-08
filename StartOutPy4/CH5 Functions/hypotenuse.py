# This program calculates the length of a right
# triangle's hypotenuse.
import math

def main():
    # Get the length of the triangle's two sides.
    a = float(input('Enter the length of the side A: '))
    b = float(input('Enter the length of the side A: '))

    # Calculate the length of the hypotenuse.
    c = math.hypot(a,b)

    # Display the length of the hypotenuse.
    print('The length of the hypotenuse is', c)

# Call the main function.
main()