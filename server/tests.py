import unittest
from engine import Minimax


class TestPuzzles(unittest.TestCase):
    def test_mate_in_two_puzzles(self):
        model = Minimax(
            depth=4,
            fen="r2qk2r/pb4pp/1n2Pb2/2B2Q2/p1p5/2P5/2B2PPP/RN2R1K1 w - - 1 0",
        )
        move = model.get_best_move()
        self.assertEqual(move.uci(), "f5g6")

    def test_mate_in_one(self):
        model = Minimax(
            depth=4,
            fen="6k1/8/8/5r2/8/8/4r3/2K5 b - - 1 1"
        )
        move = model.get_best_move()
        self.assertEqual(move.uci(), "f5f1")


if __name__ == "__main__":
    unittest.main()
