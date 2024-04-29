from flask import Flask, request
from flask_cors import CORS
import chess
import random

app = Flask(__name__)
CORS(app)


@app.route('/best-move', methods=['POST'])
def best_move():
    fen = request.json['fen']
    board = chess.Board(fen)
    moves = list(board.legal_moves)
    randomIndex = random.randint(0, len(moves)-1)
    best_move = moves[randomIndex]
    print(best_move)
    return {"best_move": best_move.uci()}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
