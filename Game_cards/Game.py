from Game_cards.Card import Card
from Game_cards.DeckOfCards import DeckOfCards
from Game_cards.Player import Player
from Game_cards.CardGame import CardGame

player1 = Player('Gal',26)
player2 = Player('Yuval',26)


game = CardGame(player1.name,player2.name,26)


print(f"{game.player1}\n{game.player2}")

for i in range(10):
    a = game.player1.get_card()
    b = game.player2.get_card()
    print(f"{game.player1.name}: {a}\t{game.player2.name}: {b}")
    if a.__gt__(b):
        print(f"{game.player1.name} wins the round")
    else:
        print(f"{game.player2.name} wins the round")








