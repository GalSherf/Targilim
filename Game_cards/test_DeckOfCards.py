from unittest import TestCase
from Game_cards.Card import Card
from Game_cards.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):

    def setUp(self):
        print('Set Up')
        self.deck1 = DeckOfCards()


    def test__init__(self):
        self.assertEqual(len(self.deck1.Deck_of_cards),52)



    def test_cards_shuffle(self):
        self.deck2 = DeckOfCards()
        self.assertNotEqual(self.deck1.Deck_of_cards,self.deck1.cards_shuffle())
        self.assertNotEqual(self.deck2.Deck_of_cards[5],self.deck1.Deck_of_cards[5])


    def test_deal_one(self):
        self.card = self.deck1.deal_one()
        self.assertNotIn(self.card,self.deck1.Deck_of_cards)
