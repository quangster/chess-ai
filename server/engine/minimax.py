from typing import Optional, List
import chess
import chess.polyglot
import os

from .evaluate import evaluate_board, get_ordered_moves
from .score import MATE_SCORE, MATE_THRESHOLD
from .base import Engine


class Minimax(Engine):
    open_reader = chess.polyglot.open_reader(os.path.join('open', 'Human.bin'))

    def __init__(
        self,
        fen: Optional[str] = chess.STARTING_FEN,
        depth: int = 3,
        debug: bool = True
    ) -> None:
        super().__init__(fen, debug)
        self.depth = depth

    def get_order_moves(self, board: chess.Board) -> List[chess.Move]:
        return get_ordered_moves(board)
        return list(board.legal_moves)

    def get_best_move(self) -> chess.Move:
        self.debug_info['depth'] = self.depth
        self.debug_info['nodes'] = 0
        opening_move = self.open_reader.get(self.board)
        if opening_move:
            return opening_move.move
        maximize = self.board.turn == chess.WHITE
        best_move_score = -float('inf')
        if not maximize:
            best_move_score = float('inf')
        moves = self.get_order_moves(self.board)
        best_move_found = moves[0]
        for move in moves:
            self.board.push(move)
            if self.board.can_claim_draw():
                value = 0.0
            else:
                value = self._minimax(
                    self.board,
                    self.depth-1,
                    not maximize
                )
            self.board.pop()
            if maximize and value >= best_move_score:
                best_move_score = value
                best_move_found = move
            elif not maximize and value <= best_move_score:
                best_move_score = value
                best_move_found = move
        return best_move_found

    def _minimax(
        self,
        board: chess.Board,
        depth: int,
        is_maximize_player: bool
    ) -> float:
        self.debug_info['nodes'] += 1
        if board.is_checkmate():
            return -MATE_SCORE if is_maximize_player else MATE_SCORE
        elif board.is_game_over():
            return 0

        if depth == 0:
            return evaluate_board(board)

        if is_maximize_player:
            best_move_score = -float('inf')
            moves = self.get_order_moves(board)
            for move in moves:
                board.push(move)
                curr_move_score = self._minimax(
                    board,
                    depth-1,
                    not is_maximize_player
                )
                if curr_move_score > MATE_THRESHOLD:
                    curr_move_score -= 1
                elif curr_move_score < -MATE_THRESHOLD:
                    curr_move_score += 1
                best_move_score = max(best_move_score, curr_move_score)
                board.pop()
            return best_move_score
        else:
            best_move_score = float('inf')
            moves = self.get_order_moves(board)
            for move in moves:
                board.push(move)
                curr_move_score = self._minimax(
                    board,
                    depth-1,
                    not is_maximize_player
                )
                if curr_move_score > MATE_THRESHOLD:
                    curr_move_score -= 1
                elif curr_move_score < -MATE_THRESHOLD:
                    curr_move_score += 1
                best_move_score = min(best_move_score, curr_move_score)
                board.pop()
            return best_move_score
