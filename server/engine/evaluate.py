import chess

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


def evaluate_piece(piece: chess.Piece, square: chess.Square, end_game: bool = False) -> int:
    piece_type = piece.piece_type
    is_white_piece = piece.color == chess.WHITE
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

        value = PIECE_VALUES[piece.piece_type] + evaluate_piece(piece, square, end_game)
        total += value if piece.color == chess.WHITE else -value
    return total

def check_end_game(board: chess.Board) -> bool:
    """
    Check end game:
    - Both side have no queens or
    - Every side which has a queen has additionally no other pieces or one minorpiece maximum
    """
    queens = 0
    minors = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type == chess.QUEEN:
            queens += 1
        if piece and (piece.piece_type == chess.BISHOP or piece.piece_type == chess.KNIGHT):
            minors += 1
    if queens == 0 or (queens == 2 and minors <= 1):
        return True
    return False