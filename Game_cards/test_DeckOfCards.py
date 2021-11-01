from unittest import TestCase
from Game_cards.Card import Card
from Game_cards.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):

    def setUp(self):
        print('Set Up')
        self.deck1 = DeckOfCards()

    # check that there are 52 cards in a deck
    def test__init__(self):
        self.assertEqual(len(self.deck1.Deck_of_cards),52)


    # check the cards_shuffle method, shuffled deck isn't equal to regular deck
    def test_cards_shuffle(self):
        self.deck2 = DeckOfCards()
        self.assertNotEqual(self.deck1.Deck_of_cards,self.deck1.cards_shuffle())
        self.assertNotEqual(self.deck2.Deck_of_cards[5],self.deck1.Deck_of_cards[5])


    # check the deal_one method, the pulled card won't be in the deck anymore
    def test_deal_one(self):
        self.card = self.deck1.deal_one()
        self.assertNotIn(self.card,self.deck1.Deck_of_cards)
