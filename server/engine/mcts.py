import chess
import math
import random
from typing import List
import os
from .base import Engine


class Node:
    def __init__(self, board: chess.Board, parent=None):
        self.board = board
        self.parent = parent
        self.child = []
        self.wins = 0
        self.visits = 0
        self.non_visited_move = list(self.board.legal_moves)
        self.visited_move = []

    def is_leaf_node(self):
        return len(self.non_visited_move) != 0

    def is_terminal_node(self):
        return len(self.non_visited_move) == 0 and len(self.visited_move) == 0


class MonteCarloTreeSearch(Engine):
    open_reader = chess.polyglot.open_reader(os.path.join("open", "Human.bin"))

    def __init__(self, fen, C=1.4142, simulations=1000, debug=True):
        super().__init__(fen, debug)
        self.board = chess.Board(fen)
        self.C = C
        self.simulations = simulations

    def uct_value(self, node: Node, parent: Node) -> float:
        return (node.wins / node.visits) + self.C * math.sqrt(math.log(parent.visits) / node.visits)

    def select(self, node: Node):
        if (node.is_leaf_node() or node.is_terminal_node()):
            return node
        max_uct_child = None
        max_uct_val = -1000000
        for move, child in node.visited_move:
            uct_val_child = self.uct_value(child, node)
            if max_uct_val < uct_val_child:
                max_uct_child = child
                max_uct_val = uct_val_child
        if max_uct_child is None:
            raise ValueError("Error value")
        else:
            return self.select(max_uct_child)

    def expand(self, node: Node):
        move = node.non_visited_move.pop()
        board = node.board.copy()
        board.push(move)
        child_node = Node(board)
        child_node.parent = node
        node.visited_move.append((move, child_node))
        return child_node

    def simulate(self, node: Node, player):
        board = node.board.copy()
        while board.outcome(claim_draw=True) is None:
            legal_moves = list(board.legal_moves)
            move = random.choice(legal_moves)
            board.push(move)

        outcome = board.outcome(claim_draw=True)
        if outcome.winner is None:
            return 0.5
        elif outcome.winner == player:
            return 1
        else:
            return 0

    def backpropagate(self, node: Node, payout):
        node.wins += payout
        node.visits += 1
        if node.parent is not None:
            self.backpropagate(node.parent, payout)

    def get_order_moves(self, board: chess.Board) -> List[chess.Move]:
        return list(board.legal_moves)

    def get_best_move(self):
        opening_move = self.open_reader.get(self.board)
        if opening_move:
            return opening_move.move

        root = Node(self.board)
        player = self.board.turn

        for i in range(self.simulations):
            node = self.select(root)
            if not node.is_terminal_node():
                node = self.expand(node)
            payout = self.simulate(node, player)
            self.backpropagate(node, payout)
        # print(root.wins)
        # print(root.visits)
        best_move = None
        best_score = -1
        for move, child in root.visited_move:
            # print(move, child.wins, child.visits)
            if child.wins > best_score:
                best_move = move
                best_score = child.wins
        return best_move


if __name__ == "__main__":
    mtcs = MonteCarloTreeSearch(
        fen="r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R w KQkq - 1 0",
        simulations=500
    )
    best_move = mtcs.get_best_move()
    print(best_move)
