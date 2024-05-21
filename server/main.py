from flask import Flask, request
from flask_cors import CORS
from engine import AlphaBeta, Minimax, MonteCarloTreeSearch

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
    if "depth" in request.json:
        depth = request.json["depth"]
    else:
        depth = 3
    model = AlphaBeta(fen, depth=depth)
    best_move = model.play()
    info = model.get_debug_info()
    return {
        "best_move": best_move.uci(),
        "info": info
    }


@app.route('/minimax', methods=['POST'])
def get_move_by_minimax():
    fen = request.json['fen']
    if "depth" in request.json:
        depth = request.json["depth"]
    else:
        depth = 3
    model = Minimax(fen, depth=depth)
    best_move = model.play()
    info = model.get_debug_info()
    return {
        "best_move": best_move.uci(),
        "info": info
    }


@app.route("/mcts", methods=["POST"])
def get_move_by_mcts():
    fen = request.json["fen"]
    if "C" in request.json:
        C = request.json["C"]
    else:
        C = 1.4142
    if "simulations" in request.json:
        simulations = request.json["C"]
    else:
        simulations = 300
    model = MonteCarloTreeSearch(fen, C, simulations)
    best_move = model.play()
    info = model.get_debug_info()
    return {"best_move": best_move.uci(), "info": info}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
