from unittest import TestCase,mock
from unittest.mock import patch
from Game_cards import Player

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
        self.Dani = Player('Dani',15)
        self.assertEqual('Dani',self.Dani.name)
        self.assertEqual(self.Dani.num_of_cards,15)

    # check for invalid values for player argument - num_of_cards
    def test__init__3(self):
        self.Dan = Player('Dan', 50)
        self.assertEqual(self.Dan.num_of_cards, 26)
        self.Aviv = Player('Aviv',-5)
        self.assertEqual(self.Aviv.num_of_cards,26)



    def test_get_card(self):
        self.player.num_of_cards = 1
        self.player.set_hand(self.deck)
        self.assertEqual(self.player.pack_of_cards[0],self.player.get_card())
        self.assertIn(self.player.get_card(),self.player.pack_of_cards)


    def test_add_card(self):
        self.card = Card(9, '♣')
        self.player.add_card(self.card)
        self.assertIn(self.card,self.player.pack_of_cards)
        self.card2 = Card(4, '♣')
        self.player.add_card(self.card2)
        self.assertIn(self.card2, self.player.pack_of_cards) and self.assertIn(self.card,self.player.pack_of_cards)

    def test_add_card2(self):
        with self.assertRaises(ValueError):
            self.card = Card(20, '♣')
            self.player.add_card(self.card)
            self.assertIn(self.card, self.player.pack_of_cards)

    def test_add_card3(self):
        self.player.num_of_cards = 3
        self.card = Card(8, '♣')
        with self.assertRaises(ValueError):
            self.player.add_card(self.card)
            self.player.add_card(self.card)


    @mock.patch('Game_cards.DeckOfCards.DeckOfCards.deal_one', return_value=Card(9, '♣'))
    def test_set_hand(self, mock_card):
        self.player.num_of_cards = 1
        self.player.set_hand(self.deck)
        self.assertIn(mock_card.return_value,self.player.pack_of_cards)
        self.assertEqual(mock_card.return_value,Card(9, '♣'))
        self.assertNotIn(Card(7, '♣'),self.player.pack_of_cards)
