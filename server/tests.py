import unittest
from engine import Minimax, AlphaBeta, MonteCarloTreeSearch

# https://wtharvey.com/m8n2.txt
MATE_IN_2 = [
    ["r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R w KQkq - 1 0", "d5f6"],
    ["r2qk2r/pb4pp/1n2Pb2/2B2Q2/p1p5/2P5/2B2PPP/RN2R1K1 w - - 1 0", "f5g6"],
    ["5bk1/6p1/5PQ1/pp4Pp/2p4P/P2r4/1PK5/8 w - - 1 0", "f6f7"],
    ["5bk1/R4p1p/6p1/8/3p2K1/1Q4P1/1P3P1q/2r5 b - - 0 1", "h2h5"],
    ["1rb4r/pkPp3p/1b1P3n/1Q6/N3Pp2/8/P1P3PP/7K w - - 1 0", "b5d5"],
    ["4kb1r/p2n1ppp/4q3/4p1B1/4P3/1Q6/PPP2PPP/2KR4 w k - 1 0", "b3b8"],
]

# https://wtharvey.com/m8n3.txt
MATE_IN_3 = [
    ["r1b1kb1r/pppp1ppp/5q2/4n3/3KP3/2N3PN/PPP4P/R1BQ1B1R b kq - 0 1", "f8c5"],
    ["r3k2r/ppp2Npp/1b5n/4p2b/2B1P2q/BQP2P2/P5PP/RN5K w kq - 1 0", "c4b5"],
    ["r1b3kr/ppp1Bp1p/1b6/n2P4/2p3q1/2Q2N2/P4PPP/RN2R1K1 w - - 1 0", "c3h8"],
    ["r2n1rk1/1ppb2pp/1p1p4/3Ppq1n/2B3P1/2P4P/PP1N1P1K/R2Q1RN1 b - - 0 1", "f5f2"],
    ["rn3rk1/p5pp/2p5/3Ppb2/2q5/1Q6/PPPB2PP/R3K1NR b - - 0 1", "c4f1"],
]

# https://wtharvey.com/m8n4.txt
MATE_IN_4 = [
    ["r5rk/2p1Nppp/3p3P/pp2p1P1/4P3/2qnPQK1/8/R6R w - - 1 0", "h6g7"],
    ["1r2k1r1/pbppnp1p/1b3P2/8/Q7/B1PB1q2/P4PPP/3R2K1 w - - 1 0", "a4d7"],
    ["Q7/p1p1q1pk/3p2rp/4n3/3bP3/7b/PP3PPK/R1B2R2 b - - 0 1", "d4f2"],
    ["r1bqr3/ppp1B1kp/1b4p1/n2B4/3PQ1P1/2P5/P4P2/RN4K1 w - - 1 0", "e4e5"],
    ["r1b3kr/3pR1p1/ppq4p/5P2/4Q3/B7/P5PP/5RK1 w - - 1 0", "e7g7"],
]


class TestPuzzles(unittest.TestCase):
    def test_mate_in_2_minimax(self):
        for e in MATE_IN_2:
            minimax = Minimax(fen=e[0], depth=3)
            move = minimax.get_best_move()
            self.assertEqual(move.uci(), e[1])

    def test_mate_in_2_alphabeta(self):
        for e in MATE_IN_2:
            alphabeta = AlphaBeta(fen=e[0], depth=3)
            move = alphabeta.get_best_move()
            self.assertEqual(move.uci(), e[1])

    def test_mate_in_3_alphabeta(self):
        for e in MATE_IN_3:
            alphabeta = AlphaBeta(fen=e[0], depth=5)
            move = alphabeta.get_best_move()
            self.assertEqual(move.uci(), e[1])

    # def test_mate_in_4_alphabeta(self):
    #     for e in MATE_IN_4:
    #         alphabeta = AlphaBeta(fen=e[0], depth=5)
    #         move = alphabeta.get_best_move()
    #         self.assertEqual(move.uci(), e[1])

    def test_mate_in_2_mcts(self):
        for e in MATE_IN_2:
            mcts = MonteCarloTreeSearch(fen=e[0], simulations=1000)
            move = mcts.get_best_move()
            self.assertEqual(move.uci(), e[1])


if __name__ == "__main__":
    unittest.main()
