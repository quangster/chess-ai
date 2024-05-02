from flask import Flask, request
from flask_cors import CORS
import chess
from engine import min_maxN

app = Flask(__name__)
CORS(app)


@app.route('/best-move', methods=['POST'])
def best_move():
    fen = request.json['fen']
    board = chess.Board(fen)
    best_move = min_maxN(board, 3)
    return {"best_move": best_move.uci()}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
