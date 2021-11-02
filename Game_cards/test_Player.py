from unittest import TestCase,mock
from unittest.mock import patch
from Game_cards.Player import Player
from Game_cards.DeckOfCards import DeckOfCards
from Game_cards.Card import Card

class TestPlayer(TestCase):

    def setUp(self):
        self.player = Player('Avi',26)
        self.deck = DeckOfCards()
        print('setUp')

    def tearDown(self):
        print("tearDown")

    # check for invalid types of arguments for player
    def test__init__(self):
        with self.assertRaises(TypeError):
            self.player.name = Player(23,26)
        with self.assertRaises(TypeError):
            self.player.num_of_cards = Player('Avi','Avi')

    # check for valid arguments for player
    def test__init__2(self):
        self.player1 = Player('Dani',15)
        self.assertEqual('Dani',self.player1.name)
        self.assertEqual(self.player1.num_of_cards,15)
        self.assertNotEqual(self.player1.num_of_cards, 26)

    # check for invalid values for player argument - num_of_cards
    def test__init__3(self):
        self.player1 = Player('Dan', 27)
        self.player2 = Player('Aviv',9)
        self.player3 = Player('Muki', 0)
        self.assertEqual(self.player1.num_of_cards, 26)
        self.assertEqual(self.player2.num_of_cards,26)
        self.assertEqual(self.player3.num_of_cards, 26)

    # check that the card from deal_one method is in player's pack
    @mock.patch('Game_cards.DeckOfCards.DeckOfCards.deal_one', return_value=Card(9, '♣'))
    def test_set_hand(self, mock_card):
        self.player.num_of_cards = 1
        self.player.set_hand(self.deck)
        self.assertIn(mock_card.return_value,self.player.pack_of_cards)
        self.assertEqual(mock_card.return_value,Card(9, '♣'))
        self.assertNotIn(Card(7, '♣'),self.player.pack_of_cards)
        self.assertEqual(len(self.player.pack_of_cards),1)

    # deals one card to player, and check if the returned card is equal to it
    def test_get_card(self):
        self.player.num_of_cards = 1
        self.player.set_hand(self.deck)
        self.assertEqual(self.player.pack_of_cards[0],self.player.get_card())
        self.assertIn(self.player.get_card(),self.player.pack_of_cards)

    # gets two cards from deck and check if they been added to player's pack
    def test_add_card(self):
        self.card = Card(9, '♣')
        self.player.add_card(self.card)
        self.assertIn(self.card,self.player.pack_of_cards)
        self.card2 = Card(4, '♣')
        self.player.add_card(self.card2)
        self.assertIn(self.card2, self.player.pack_of_cards) and self.assertIn(self.card,self.player.pack_of_cards)

    # check for invalid card
    def test_add_card2(self):
        with self.assertRaises(ValueError):
            self.card = Card(20, '♣')
            self.player.add_card(self.card)
            self.assertIn(self.card, self.player.pack_of_cards)

    # check that same card can not be inserted to player's pack more then one time
    def test_add_card3(self):
        self.card = Card(8, '♣')
        with self.assertRaises(ValueError):
            self.player.add_card(self.card)
            self.player.add_card(self.card)

