# The deal_cards function deals a specified number of cards
# from the deck. 9-1

def deal_cards(deck, number):
    # Initialize an accumulator for the hand value.
    hand_value = 0

    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    if number > len(deck):
        number = len(deck)

    # Deal the cards and accumulate their values.
    for count in range(number):
        card, value = deck.popitem()
        print(card)
        hand_value += value

    # Display the value of the hand.
    print('Value of this hand: ', hand_value)

# Call the main function.
main()