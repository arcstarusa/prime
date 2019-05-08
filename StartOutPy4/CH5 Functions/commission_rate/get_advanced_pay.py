# The get_advanced_pay function gets the amount of
# advanced pay given to the salesperson and returns
# that amount.
def get_advanced_pay():
    # Get the amount of advanced pay.
    print('Enter the amount of advanced pay, or')
    print('enter 0 if no advnaced pay was given.')
    advanced = float(input('Advanced pay: '))

    # Returned the amount entered.
    return advanced