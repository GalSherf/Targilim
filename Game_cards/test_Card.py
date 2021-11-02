from unittest import TestCase
from Game_cards.Card import Card


class TestCard(TestCase):

    def setUp(self):
        print('setUp')
        self.card = Card(9, "🔶")

    def tearDown(self):
        print("tearDown")

    # check for a valid value and suit for card
    def test__init__(self):
        self.assertEqual(self.card.value, 9)
        self.assertEqual(self.card.suit, "🔶")

    # check for invalid value or suit for card
    def test__init__2(self):
        with self.assertRaises(TypeError):
            self.card1 = Card(7, "abc")
        with self.assertRaises(TypeError):
            self.card2 = Card("abc", "🔶")
        with self.assertRaises(ValueError):
            self.card3 = Card(15, "🔶")
        with self.assertRaises(ValueError):
            self.card4 = Card(-2, "🔶")

    # test the __gt__ method, when card is bigger then other card
    def test__gt__(self):
        self.card2 = Card(9, "♣")
        self.assertEqual(self.card.value, self.card2.value)
        self.assertNotEqual(self.card.suit, self.card2.suit)
        self.assertIsNot(self.card, self.card2)
        self.assertGreater(self.card2, self.card)
        self.assertTrue(self.card2.__gt__(self.card))
        self.assertFalse(self.card.__gt__(self.card2))

    # test the __eq__ method, when card is equal to other card
    def test__eq__(self):
        self.card1 = Card(9, "🔶")
        self.card2 = Card(9, "♣")
        self.card3 = Card(8, "🔶")
        self.assertEqual(self.card,self.card1)
        self.assertTrue(self.card.__eq__(self.card1))
        self.assertFalse(self.card.__eq__(self.card2))
        self.assertFalse(self.card.__eq__(self.card3))