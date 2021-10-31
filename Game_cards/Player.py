from Game_cards.Card import Card
from Game_cards.DeckOfCards import DeckOfCards
import random

class Player:

    def __init__(self,name, num_of_cards=26):
        self.name=name
        self.num_of_cards=num_of_cards
        if type(self.name) != str:
            raise TypeError('invalid type for player name')
        if type(self.num_of_cards) != int:
            raise TypeError('invalid type for number of cards')
        if self.num_of_cards>26 or self.num_of_cards<10:
            self.num_of_cards=26
        self.pack_of_cards=[]


    def __repr__(self):
        return f"{self.name}, {len(self.pack_of_cards)} {self.pack_of_cards}"

    # a method that deals cards to player
    def set_hand(self, deck_of_cards:DeckOfCards):
        for i in range(self.num_of_cards):
            self.pack_of_cards.append(deck_of_cards.deal_one())

    # a method that takes out a random card from player's hand
    def get_card(self):
        return random.choice(self.pack_of_cards)

    # a method that add one card to player's hand
    def add_card(self, card:Card):
        self.pack_of_cards.append(card)