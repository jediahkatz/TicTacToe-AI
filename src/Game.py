from GameState import *

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
                    game_state.x_move(tile=tile)
                    return
                except ValueError:
                    print("That tile is already occupied! ", end="")
            else:
                print("That is not a valid tile. ", end="")
        except ValueError:
            print("That is not a valid tile. ", end="")


print (game_state.current_player)
while not game_state.is_full():
    game_state.print()
    next_move()
    print(game_state.winner())