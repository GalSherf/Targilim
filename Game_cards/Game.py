from Game_cards.Card import Card
from Game_cards.DeckOfCards import DeckOfCards
from Game_cards.Player import Player
from Game_cards.CardGame import CardGame

player1 = Player(input("enter name: "),26)
player2 = Player(input("enter name: "),26)


game = CardGame(player1.name,player2.name,26)


print(f"{game.player1}\n{game.player2}")


