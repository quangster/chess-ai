import chess
import random
from copy import deepcopy

import chess.polyglot


reader = chess.polyglot.open_reader('engine/baron30.bin')


def random_agent(board: chess.Board):
    return random.choice(list[board.legal_moves])


scoring = {
    "p": -1,
    "n": -3,
    "b": -3,
    "r": -5,
    "q": -9,
    "k": 0,
    "P": 1,
    "N": 3,
    "B": 3,
    "R": 5,
    "Q": 9,
    "K": 0
}


def eval_board(board: chess.Board) -> int:
    score = 0
    pieces = board.piece_map()
    for key in pieces:
        score += scoring[str(pieces[key])]
    return score


def eval_space(board: chess.Board):
    no_moves = len(list(board.legal_moves))
    value = (no_moves/(20+no_moves))
    if board.turn:
        return value
    else:
        return -value


def get_best_move_by_minimax(board: chess.Board):
    print(board.turn)
    moves = list(board.legal_moves)
    scores = []
    for move in moves:
        temp = deepcopy(board)
        temp.push(move)

        scores.append(eval_board(temp))
    if board.turn:
        best_move = moves[scores.index(max(scores))]
    else:
        best_move = moves[scores.index(min(scores))]
    return best_move


def min_max2(board: chess.Board):
    moves = list(board.legal_moves)
    scores = []
    for move in moves:
        temp = deepcopy(board)
        temp.push(move)

        temp_best_move = get_best_move_by_minimax(temp)
        temp.push(temp_best_move)
        scores.append(eval_board(temp))

    if board.turn:
        best_move = moves[scores.index(max(scores))]
    else:
        best_move = moves[scores.index(min(scores))]
    return best_move


def min_maxN(board: chess.Board, depth):
    opening_move = reader.get(board)
    if opening_move:
        return opening_move.move
    moves = list(board.legal_moves)
    scores = []
    for move in moves:
        temp = deepcopy(board)
        temp.push(move)

        outcome = temp.outcome()

        if not outcome:
            if depth > 1:
                temp_best_move = min_maxN(temp, depth-1)
                temp.push(temp_best_move)
            scores.append(eval_board(temp))
        elif temp.is_checkmate():
            return move
        else:
            val = 1000
            if board.turn:
                scores.append(-val)
            else:
                scores.append(val)
        scores[-1] = scores[-1] + eval_space(temp)

    if board.turn:
        best_move = moves[scores.index(max(scores))]
    else:
        best_move = moves[scores.index(min(scores))]
    return best_move
