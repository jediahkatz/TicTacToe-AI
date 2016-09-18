# 3 by 3 game board
class Board:

    # an array with 9 values representing the board state
    # the board is counted from left to right
    # can have " ", "X", or "O"
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def print(self):
        """
        Print this board to the console.
        """
        for i in range(3):
            print("  " + self.board[i*3] + "  " + "|" + "  " + self.board[i*3+1] + "  " + "|" + "  " + self.board[i*3+2] + "  ")
            if i < 2: print("-----------------")

    def x_move(self,tile):
        """
        Adds an X to the specified tile. Throws an exception if the tile is occupied.
        :param tile: The tile to place an X on. [0 - 8]
        """
        if self.board[tile] == " ":
            self.board[tile] = "X"
        else:
            raise Exception("Tile " + tile + " is already occupied!")

    def o_move(self,tile):
        """
        Adds an X to the specified tile. Throws an exception if the tile is occupied.
        :param tile: The tile to place an O on. [0 - 8]
        """
        if self.board[tile] == " ":
            self.board[tile] = "O"
        else:
            raise Exception("Tile " + str(tile) + " is already occupied!")

gameboard = Board()
gameboard.x_move(0)
gameboard.o_move(2)
gameboard.print()