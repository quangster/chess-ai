import { useState } from "react";
import { Chess } from "chess.js";
import { Chessboard } from "react-chessboard";

export default function ChessBoard() {
  const [game, setGame] = useState(new Chess());

  const makeAMove = (move) => {
    try {
      const result = game.move(move);
      setGame(new Chess(game.fen()));
      return result;
    } catch (error) {
      game.undo();
    }
  };

  const makeRandomMove = () => {
    const possibleMoves = game.moves();

    if (game.isGameOver() || game.isDraw() || possibleMoves.length === 0) {
      return;
    }
    const randomIndex = Math.floor(Math.random() * possibleMoves.length);
    makeAMove(possibleMoves[randomIndex]);
  };

  const onDrop = async (sourceSquare, targetSquare) => {
    const move = makeAMove({
      from: sourceSquare,
      to: targetSquare,
      promotion: "q",
    });
    // console.log(game.fen());
    if (move === null) return false;
    // setTimeout(makeRandomMove, 200);
    const response = await fetch('http://localhost:5000/best-move', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ fen: game.fen() }),
    });

    if (!response.ok) {
      throw new Error('Failed')
    }

    const data = await response.json();
    const bestMove = data.best_move;
    game.move(bestMove);
    setGame(new Chess(game.fen()));
    return true;
  };

  return (
    <div>
      <Chessboard
        position={game.fen()}
        onPieceDrop={onDrop}
        boardWidth={350}
        customBoardStyle={{
          borderRadius: "4px",
          boxShadow: "0 2px 10px rgba(0, 0, 0, 0.5)",
        }}
      />
    </div>
  );
}
