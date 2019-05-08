# The get_total function accepts a list as an
# argument returns the total of the values in
# the list. 7-12
def get_total(value_list):
    # Create a variable to use as an accumulator.
    total = 0.0

    # Calculate the total of the list elements.
    for num in value_list:
        total += num

    # Return the total
    return total

# Call the main function
main()