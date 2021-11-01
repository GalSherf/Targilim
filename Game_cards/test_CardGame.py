from unittest import TestCase
from CardGame import *
from Player import *


class TestCardGame(TestCase):


    def setUp(self):
        print('Set Up')
        self.cardgame = CardGame('Gal','Dani')
        self.deck = DeckOfCards()


    def test__init__(self):
        pass

    def test_new_game(self):
        self.

    def test_get_winner(self):
        self.fail()
