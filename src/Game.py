from GameState import *
from random import randint
from OpponentAI import MinimaxAI

next = False
while not next:
    userInput = input("Want to go first? (y/n)\n")
    if userInput == "y":
        next = True
        first = True
    if userInput == "n":
        next = True
        first = False

game_state = State("O") if first else State("X")


def next_move():
    print("Where would you like to move next? ", end="")
    while True:
        tile = input("Choose a tile from 0 to 8.\n")
        try:
            tile = int(tile)
            if 0 <= tile <= 8:
                try:
                    game_state.o_move(tile=tile)
                    return
                except ValueError:
                    print("That tile is already occupied! ", end="")
            else:
                print("That is not a valid tile. ", end="")
        except ValueError:
            print("That is not a valid tile. ", end="")


opponent = MinimaxAI()

if not first:
    # The optimal first turn is always to choose a corner.
    # To speed things up, the opponent will choose a random
    # corner instead of minimaxing the first turn.
    corners = [0, 2, 6, 8]
    game_state.x_move(corners[randint(0,3)])

# Run game
while not game_state.winner():
    game_state.print()
    next_move()
    if not game_state.winner():
        opponent.take_turn(game_state)


winner = game_state.winner()
if winner == "Draw":
    print("\033[1mIt's a draw!\033[0m")
elif winner == "X":
    print("\033[1mSorry, you lost!\033[0m")
elif winner == "O":
    print("\033[1mYou won? Did you cheat?\033[0m")