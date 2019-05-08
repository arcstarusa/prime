# This program writes three lines of data
# to a file. 6-1
def main():
    # Open a file named philosophers.txt.
    outfile = open('Philosophers.txt', 'w')

    # Write the names of three philosphers
    # to the file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file.
    outfile.close()

# Call the main function.
main()