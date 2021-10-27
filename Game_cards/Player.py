from Game_cards.Card import Card
from Game_cards.DeckOfCards import DeckOfCards
import random

class Player:

    def __init__(self,name, num_of_cards=26):
        self.name=name
        self.num_of_cards=num_of_cards
        if self.num_of_cards>26 or self.num_of_cards<10:
            self.num_of_cards=26
        self.pack_of_cards=[]

    def __repr__(self):
        return f"{self.name}, {self.num_of_cards} {self.pack_of_cards}"

    def set_hand(self, deck_of_cards:DeckOfCards):
        for i in range(self.num_of_cards):
            self.pack_of_cards.append(deck_of_cards.deal_one())


    def get_card(self):
        return random.choice(self.pack_of_cards)

    def add_card(self, card:Card):
        self.pack_of_cards.append(card)

    def mo(self,deck_of_cards:DeckOfCards):
        set1 = set(self.pack_of_cards)
        while len(self.pack_of_cards) != self.num_of_cards:
            set1.add(deck_of_cards.deal_one())


# deck = DeckOfCards()
# muki = Player('Muki')
# print(muki.mo(deck))