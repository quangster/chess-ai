from flask import Flask, request
from flask_cors import CORS
from engine import AlphaBeta, Minimax

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def welcome():
    return {
        "message": "API Chess Engine"
    }


@app.route('/alphabeta', methods=['POST'])
def get_move_by_alphabeta():
    fen = request.json['fen']
    model = AlphaBeta(fen, depth=3)
    best_move = model.play()
    return {"best_move": best_move.uci()}


@app.route('/minimax', methods=['POST'])
def get_move_by_minimax():
    fen = request.json['fen']
    model = Minimax(fen, depth=3)
    best_move = model.play()
    return {"best_move": best_move.uci()}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
