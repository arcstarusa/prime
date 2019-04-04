def load_contacts():
    try:
        # Open the contacts.dat file.
        input_file = open(FILENAME, 'rb')
        # Unpickle the dictionary.
        contact_dct = pickle.load(input_file)
        # Close the phone_inventory.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create an empty dictionary
        contact_dct = {}
    # Return the dictionary.
    return contact_dct
