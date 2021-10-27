from Game_cards.Card import Card
from Game_cards.DeckOfCards import DeckOfCards
from Game_cards.Player import Player

class CardGame:
    def __init__(self,deck_of_cards:DeckOfCards,player1:Player,player2:Player):
        self.player1 = player1
        self.player2 = player2
        self.deck_of_cards = deck_of_cards
        pass

    # a method that shuffle and deals cards to the players
    def new_game:
        DeckOfCards.shuffle()
        Player.set_hand(DeckOfCards)

    # a method that returns the player who wins. if draw - None
    def get_winner:
        if self.player1




