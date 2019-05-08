# This program demonstrates two functions that
# have local variables with the same name. 5-5

def main():
    # Call the texas function.
    texas()
    # Call the california function.
    california()

# Definition of the texas function. It creates
# a local variables named birds.
def texas():
    birds = 5000
    print('texas has', birds, 'birds.')

# Definition of the california funciton. It also
# creates a local variable named birds.
def california():
        birds = 8000
        print('california has', birds, 'birds.')

# Call the main function.
main()
