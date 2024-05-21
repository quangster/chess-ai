import chess
from typing import List

from .score import (
    PIECE_VALUES,
    PAWN_WHITE, PAWN_BLACK,
    ROOK_WHITE, ROOK_BLACK,
    KNIGHT_WHITE, KNIGHT_BLACK,
    BISHOP_WHITE, BISHOP_BLACK,
    QUEEN_WHITE, QUEEN_BLACK,
    KING_WHITE, KING_BLACK,
    KING_END_WHITE, KING_END_BLACK,
)


def evaluate_piece(
    piece: chess.Piece,
    square: chess.Square,
    end_game: bool = False
) -> int:
    piece_type = piece.piece_type
    is_white_piece = (piece.color == chess.WHITE)
    mapping = []
    if piece_type == chess.PAWN:
        mapping = PAWN_WHITE if is_white_piece else PAWN_BLACK

    if piece_type == chess.KNIGHT:
        mapping = KNIGHT_WHITE if is_white_piece else KNIGHT_BLACK

    if piece_type == chess.BISHOP:
        mapping = BISHOP_WHITE if is_white_piece else BISHOP_BLACK

    if piece_type == chess.ROOK:
        mapping = ROOK_WHITE if is_white_piece else ROOK_BLACK

    if piece_type == chess.QUEEN:
        mapping = QUEEN_WHITE if is_white_piece else QUEEN_BLACK

    if piece_type == chess.KING:
        if end_game:
            mapping = KING_END_WHITE if is_white_piece else KING_END_BLACK
        else:
            mapping = KING_WHITE if is_white_piece else KING_BLACK
    return mapping[square]


def evaluate_board(board: chess.Board) -> float:
    total = 0
    end_game = check_end_game(board)
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue

        value = (
            PIECE_VALUES[piece.piece_type] +
            evaluate_piece(piece, square, end_game)
        )
        total += value if piece.color == chess.WHITE else -value
    return total


def move_value(board: chess.Board, move: chess.Move, endgame: bool) -> float:
    """
    How good is a move?
    A promotion is great.
    A weaker piece taking a stronger piece is good.
    A stronger piece taking a weaker piece is bad.
    Also consider the position change via piece-square table.
    """
    if move.promotion is not None:
        return -float("inf") if board.turn == chess.BLACK else float("inf")

    _piece = board.piece_at(move.from_square)
    if _piece:
        _from_value = evaluate_piece(_piece, move.from_square, endgame)
        _to_value = evaluate_piece(_piece, move.to_square, endgame)
        position_change = _to_value - _from_value
    else:
        raise Exception(f"A piece was expected at {move.from_square}")

    capture_value = 0.0
    if board.is_capture(move):
        capture_value = evaluate_capture(board, move)

    current_move_value = capture_value + position_change
    if board.turn == chess.BLACK:
        current_move_value = -current_move_value

    return current_move_value


def evaluate_capture(board: chess.Board, move: chess.Move) -> float:
    """
    Given a capturing move, weight the trade being made.
    """
    if board.is_en_passant(move):
        return PIECE_VALUES[chess.PAWN]
    _to = board.piece_at(move.to_square)
    _from = board.piece_at(move.from_square)
    if _to is None or _from is None:
        raise Exception(
            f"Pieces were expected at _both_ {move.to_square} and {move.from_square}"
        )
    return PIECE_VALUES[_to.piece_type] - PIECE_VALUES[_from.piece_type]


def get_ordered_moves(board: chess.Board) -> List[chess.Move]:
    """
    Get legal moves.
    Attempt to sort moves by best to worst.
    Use piece values (and positional gains/losses) to weight captures.
    """
    end_game = check_end_game(board)

    def orderer(move):
        return move_value(board, move, end_game)

    in_order = sorted(
        board.legal_moves, key=orderer, reverse=(board.turn == chess.WHITE)
    )
    return list(in_order)


def check_end_game(board: chess.Board) -> bool:
    """
    Check end game:
    - Both side have no queens or
    - Every side which has a queen has additionally
        no other pieces or one minorpiece maximum
    """
    queens = 0
    minors = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            if piece.piece_type == chess.QUEEN:
                queens += 1
            elif piece.piece_type == chess.BISHOP:
                minors += 1
            elif piece.piece_type == chess.KNIGHT:
                minors += 1
    if queens == 0 or (queens == 2 and minors <= 1):
        return True
    return False
