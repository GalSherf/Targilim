from Game_cards.CardGame import CardGame

name1 = input("enter player name: ")
name2 = input("enter player name: ")
game = CardGame(name1,name2)

print(f"{game.player1}\n{game.player2}")

for i in range(10):
    a = game.player1.get_card()
    b = game.player2.get_card()
    print(f"{game.player1.name}: {a}\t{game.player2.name}: {b}")
    if a.__gt__(b):
        print(f"{game.player1.name} wins the round")
        game.player1.add_card(b)
        game.player2.pack_of_cards.remove(b)
    else:
        print(f"{game.player2.name} wins the round")
        game.player2.add_card(a)
        game.player1.pack_of_cards.remove(a)

if game.get_winner() == game.player1:
    print(F"The winner is: {game.player1.name} with {len(game.player1.pack_of_cards)} cards\n{game.player1.pack_of_cards}")
elif game.get_winner() == game.player2:
    print(F"The winner is: {game.player2.name} with {len(game.player2.pack_of_cards)} cards\n{game.player2.pack_of_cards}")
elif game.get_winner()== None:
    print("nobody won this time")