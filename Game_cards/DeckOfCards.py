import random
from Game_cards.Card import Card

class DeckOfCards:

    def __init__(self):
        self.Deck_of_cards = []
        suit_list = ['Heart','Spade','Diamond','Club']
        value_list = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        for suit in suit_list:
            for value in value_list:
                card=Card(value,suit)
                self.Deck_of_cards.append(card)

    def shuffle(self):
        random.shuffle(self.Deck_of_cards)

    def deal_one(self):
        return random.choice(self.Deck_of_cards)



deck = DeckOfCards()
