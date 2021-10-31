from unittest import TestCase,mock
from unittest.mock import patch

import Game_cards.Player
from Player  import *

class TestPlayer(TestCase):

    def setUp(self):
        self.player = Player('Avi',26)
        self.deck = DeckOfCards()
        print('setUp')

    def test__init__(self):
        with self.assertRaises(TypeError):
            self.player.name = Player(23,26)
        with self.assertRaises(TypeError):
            self.player.num_of_cards = Player('Avi','Avi')


    def test__init__2(self):
        self.Dani = Player('Dani',15)
        self.assertEqual('Dani',self.Dani.name)
        self.assertEqual(self.Dani.num_of_cards,15)

    def test__init__3(self):
        self.Dan = Player('Dan', 50)
        self.assertEqual(self.Dan.num_of_cards, 26)
        self.Aviv = Player('Aviv',-5)
        self.assertEqual(self.Aviv.num_of_cards,26)



    # @mock.patch('Game_cards.DeckOfCards.DeckOfCards.deal_one',
    # return_value=Card(9, "🔶"))

    # def test_set_hand(self):
    #     with patch('Game_cards.DeckOfCards.DeckOfCards.deal_one') as mock_card:
    #         mock_card.return_value = Card(9,'♣')
    #     self.player.set_hand(self.deck)
    #     self.assertEqual(mock_card,Card(9,'♣'))


    # def test_get_card(self):
    #     self.assertNotEqual()

    def test_add_card(self):
        self.card = Card(9, '♣')
        self.player.add_card(self.card)
        self.assertIn(self.card,self.player.pack_of_cards)
        self.card2 = Card(4, '♣')
        self.player.add_card(self.card2)
        self.assertIn(self.card2, self.player.pack_of_cards) and self.assertIn(self.card,self.player.pack_of_cards)

    def test_add_card2(self):
        self.card = Card(20, '♣')
        with self.assertRaises(ValueError):
            self.player.add_card(self.card)
            self.assertIn(self.card, self.player.pack_of_cards)




