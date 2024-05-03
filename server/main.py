from flask import Flask, request
from flask_cors import CORS
from engine import Minimax

app = Flask(__name__)
CORS(app)


@app.route('/best-move', methods=['POST'])
def best_move():
    fen = request.json['fen']
    print(fen)
    model = Minimax(fen)
    best_move = model.get_best_move()
    return {"best_move": best_move.uci()}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
