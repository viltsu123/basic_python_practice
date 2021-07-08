import Card
import random

class Deck:
    '''
    The deck class that will hold 52 card objects
    '''
    def __init__(self):
        self.all_cards = []

        for suits in Card.suit:
            for rank in Card.rank:
                create_card = Card.Card(suits, rank)
                self.all_cards.append(create_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        self.all_cards.pop()

'''
deck_of_cards = Deck()
#first card will be two of hearts
print(deck_of_cards.all_cards[0])

#shuffle the deck
deck_of_cards.shuffle_deck()
#should not be two of hearts
print(deck_of_cards.all_cards[0])

#should be 52 cards
print(len(deck_of_cards.all_cards))
#deal one card, should get 51 cards
deck_of_cards.deal_one_card()
print(len(deck_of_cards.all_cards))
'''
