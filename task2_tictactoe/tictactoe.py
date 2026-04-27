import math

class TicTacToeAI:
    def __init__(self):
        self.player = 'X' # Human
        self.bot = 'O'    # AI

    def check_winner(self, board):
        """
        Check if there is a winning condition on the board.
        Returns 'X', 'O', 'Tie', or None (if game is still ongoing).
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
            [0, 4, 8], [2, 4, 6]             # diagonal
        ]

        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != '':
                return board[combo[0]]

        if '' not in board:
            return 'Tie'

        return None

    def minimax(self, board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
        """
        Minimax algorithm with Alpha-Beta Pruning.
        """
        result = self.check_winner(board)
        if result == self.bot:
            return 10 - depth
        elif result == self.player:
            return depth - 10
        elif result == 'Tie':
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == '':
                    board[i] = self.bot
                    score = self.minimax(board, depth + 1, False, alpha, beta)
                    board[i] = ''
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break # Prune
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == '':
                    board[i] = self.player
                    score = self.minimax(board, depth + 1, True, alpha, beta)
                    board[i] = ''
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break # Prune
            return best_score

    def get_best_move(self, board):
        """
        Calculate the optimal next move for the AI.
        """
        best_score = -math.inf
        move = -1

        # Prevent immediate game over calculations if board is empty (optimization)
        if board.count('') == 9:
            return 4 # Always take center if going first (though user goes first typically)

        for i in range(9):
            if board[i] == '':
                board[i] = self.bot
                score = self.minimax(board, 0, False)
                board[i] = ''
                if score > best_score:
                    best_score = score
                    move = i

        return move
