import copy


# 3 by 3 game board
class State:
    def __init__(self, starting_player):
        if starting_player == "X":
            self.current_player = "X"
        else:
            self.current_player = "O"
        # an array with 9 values representing the board state
        # the board is counted from left to right
        # can have " ", "X", or "O"
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]
        self.last_move = -1

    def print(self):
        """
        Print this board to the console.
        """
        for i in range(3):
            print("  " + self.board[i * 3] + "  " + "|"
                  + "  " + self.board[i * 3 + 1] + "  " + "|"
                  + "  " + self.board[i * 3 + 2] + "  ")
            if i < 2: print("-----------------")

    def x_move(self, tile):
        """
        Adds an X to the specified tile. Throws an exception if the tile is occupied.

        :param tile: The tile to place an X on. [0 - 8]
        """
        if self.board[tile] == " ":
            self.board[tile] = "X"
            self.last_move = tile
            self.current_player = "O"
        else:
            raise ValueError("Tile " + str(tile) + " is already occupied!")

    def o_move(self, tile):
        """
        Adds an O to the specified tile. Throws an exception if the tile is occupied.

        :param tile: The tile to place an O on. [0 - 8]
        """
        if self.board[tile] == " ":
            self.board[tile] = "O"
            self.last_move = tile
            self.current_player = "X"
        else:
            raise ValueError("Tile " + str(tile) + " is already occupied!")

    def is_full(self):
        """
        Returns true if every tile on the board is occupied.
        """
        for val in self.board:
            if val == " ":
                return False
        return True

    def get_new_state(self, move):
        """
        Returns a new State object with the specified move.

        :param move: The tile that the current player will move to.
        """
        new_state = copy.deepcopy(self)

        if self.current_player == "X":
            new_state.x_move(move)
        else:
            new_state.o_move(move)

        return new_state

    def get_open_tiles(self):
        """
        Returns a list of all unoccupied tiles.
        """
        tiles = []

        for i in range(9):
            if self.board[i] == " ":
                tiles.append(i)

        return tiles

    def winner(self):
        """
        Precondition: number of winners <= 1.
        Returns "X" if X has won. Returns "O" if O has won.
        Returns "Draw" in the event of a draw. Returns False if the game is not over.
        """
        if self.last_move == -1:
            return False

        row = self.last_move // 3
        col = self.last_move % 3
        last_moved_player = "X" if self.current_player == "O" else "O"

        # check winning row
        for i in range(row * 3, row * 3 + 3):
            if self.board[i] != last_moved_player:
                break
            if i == row * 3 + 3 - 1:
                return last_moved_player

        # check winning column
        for i in range(col, col + 7, 3):
            if self.board[i] != last_moved_player:
                break
            if i == col + 7 - 1:
                return last_moved_player

        # check winning diagonal
        if row == col:
            for i in [0, 4, 8]:
                if self.board[i] != last_moved_player:
                    break
                if i == 8:
                    return last_moved_player

        # check winning antidiagonal
        if col == 2 - row:
            for i in [2, 4, 6]:
                if self.board[i] != last_moved_player:
                    break
                if i == 6:
                    return last_moved_player

        if self.is_full():
            return "Draw"

        return False
