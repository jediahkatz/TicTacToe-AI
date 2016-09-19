def score(game_state):
    winner = game_state.winner()

    if winner == "X":
        return 10
    elif winner == "O":
        return -10
    else:
        return 0


class MinimaxAI:
    # Thanks to Jason Robert Fox for a good explanation & example of the minimax function
    def minimax(self, game_state):
        if game_state.winner():
            return score(game_state)
        moves_to_scores = {}  # dictionary that maps moves to scores

        # Map each possible move to its score
        for move in game_state.get_open_tiles():
            new_state = game_state.get_new_state(move)
            moves_to_scores[move] = self.minimax(new_state)

        if game_state.current_player == "X":
            # if it's the AI's turn, maximize score
            self.best_move = max(moves_to_scores, key=moves_to_scores.get)
            return moves_to_scores[self.best_move]
        else:
            # if it's the human's turn, minimize score
            self.best_move = min(moves_to_scores, key=moves_to_scores.get)
            return moves_to_scores[self.best_move]

    def take_turn(self, game):
        self.minimax(game)
        game.x_move(self.best_move)
