import { useState } from "react";
import { Chess } from "chess.js";
import { Chessboard } from "react-chessboard";

export default function ChessBoard() {
    const [game, setGame] = useState(new Chess());
    const [customSquareStyles, setCustomSquareStyles] = useState({})

    const makeAMove = (move) => {
        try {
            const gameCopy = new Chess(game.fen())
            const result = gameCopy.move(move);
            if (result) {
                game.move(move)
                setGame(gameCopy);
            }
            return result;
        } catch (error) {
            game.undo();
        }
    };

  // Function to handle the beginning of a drag event on a piece
    const onDragBegin = (piece, sourceSquare) => {
        const moves = game.moves({ square: sourceSquare, verbose: true });
        const newSquareStyles = moves.reduce((styles, move) => {
            styles[move.to] = { backgroundColor: 'rgba(0, 0, 255, 0.5)' };
            return styles;
        }, {});
        setCustomSquareStyles(newSquareStyles);
    };

    // Function to reset custom square styles when dragging ends
    const onDragEnd = () => {
        setCustomSquareStyles({});
    };

    // Function to handle the drop of a piece
    const onDrop = async (sourceSquare, targetSquare, piece) => {
        const move = makeAMove({
            from: sourceSquare,
            to: targetSquare,
            promotion: "q" // Always promote to a queen for simplicity
        });

        if (!move) return false;

        // Fetch the best move from an external API
        try {
            const response = await fetch('http://localhost:5000/best-move', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ fen: game.fen() })
            });

            if (!response.ok) throw new Error('Network response was not ok.');

            const data = await response.json();
            game.move(data.best_move);
            setGame(new Chess(game.fen()));
        } catch (error) {
            console.error("Failed to fetch the best move:", error);
        }

        return true;
    };

    return (
        <div>
            <Chessboard
                position={game.fen()}
                onPieceDrop={onDrop}
                boardWidth={500}
                onPieceDragBegin={onDragBegin}
                onPieceDragEnd={onDragEnd}
                customSquareStyles={customSquareStyles}
                customBoardStyle={{
                    borderRadius: "4px",
                    boxShadow: "0 2px 10px rgba(0, 0, 0, 0.5)"
                }}
            />
        </div>
    );
    }