# The get_scores function gets a series of test
# scores from the user and sotes them in a list.
# A reference to the list is returned. 7-12
def get_scores():
    # Create an empty list.
    test_scores = []

    # Create a variable to control the loop.
    again = 'y'

    # Get the scores from the user and add them to
    # the list.
    while again == 'y':
        # Get a score and add it to the list.
        value = float(input('Enter a test score: '))
        test_scores.append(value)

        # Want to do this again?
        print('Do you want to add another score?')
        again = input('y = yes, anything else = no: ')
        print()

    # Return the list.
    return test_scores
