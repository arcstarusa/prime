# This program displays five random
# numbers in the range of 1 through 100. 5-18
import random

def main():
    for count in range(5):
        print(random.randint(1,100))

# Call the main function
main()