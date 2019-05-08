# This program demonstrates object unpickling. 9-5
import pickle

# main function
def main():
    end_fo_file = False # To indicate end of file

    # Open a file for binary readin.
    input_file = open('info.dat', 'rb')

    # Read to the endo f the file.
    while not end_of_file:
        try:
            # unpickle the next object.
            person = pickle.load(input_file)
            # Display the object.
            display_data(person)
        except EOFError:
                # Set the flag to indicate the end
                # of the file has been reached.
                end_of_file = True

# Close the file.
input_file.close()
# The display_data function dispays the person data
# in the dictionry that is passed as an argument.
def display_data(person):
         print('Name:', person['name'])
         print('Age:', person['age'])
         print('Weight:', person ['weight'])
         print()

# Call the main function.
main()