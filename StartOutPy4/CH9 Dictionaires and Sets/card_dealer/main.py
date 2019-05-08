# This program uses a dictionary as a deck of cards. 9-1
def main():
    # Create a deck of cards.
    deck = create_deck()

    # Get the number of cards to deal.
    num_cards = int (input('How many cards should I deal? '))

    # Deal the cards.
    deal_cards(deck, num_cards)