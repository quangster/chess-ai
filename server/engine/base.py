from abc import ABC, abstractmethod
import chess
import time
from typing import Dict, Any, Optional

import chess.polyglot


class Engine(ABC):
    debug_info: Dict[str, Any] = {}

    def __init__(
        self,
        fen: Optional[str] = chess.STARTING_FEN,
        debug: bool = True
    ) -> None:
        self.board = chess.Board(fen)
        self.debug = debug

    def play(self) -> chess.Move:
        self.debug_info.clear()
        start_time = time.time()
        move = self.get_best_move()
        self.debug_info['time'] = time.time() - start_time
        if self.debug:
            print(f"INFO: {self.debug_info}")
        return move

    @abstractmethod
    def get_best_move(self) -> chess.Move:
        pass
