import chess
import random


def get_best_move_by_random(board: chess.Board):
    moves = list(board.legal_moves)
    random_index = random.randint(0, len(moves)-1)
    best_move = moves[random_index]
    return best_move
