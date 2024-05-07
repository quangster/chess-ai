import { useState } from "react";
import { Chess } from "chess.js";
import { Chessboard } from "react-chessboard";

const ControlPanel = ({resetBoard,undoBoard, DisplayHistory}) => {

    return <div className="relative flex justify-center  h-[500px] bg-[#252622] rounded-md">
                <div className="mt-4 h-[400px] w-[350px] mx-2 overflow-x-hidden overflow-y-auto custom-scrollbar ">
                    <DisplayHistory/>
                </div>
                <div className="absolute bottom-4 grid grid-cols-[100px_100px_100px] gap-2">
                    <div id="reset_btn" onClick={resetBoard} className="bg-[#302E2B] hover:bg-[#423f3b] flex justify-center items-center py-2 rounded">
                        <svg width="35px" height="35px" viewBox="-2 -2 24.00 24.00" xmlns="http://www.w3.org/2000/svg" fill="#302E2B" stroke="#302E2B" stroke-width="0.48" transform="rotate(0)matrix(1, 0, 0, 1, 0, 0)"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round" stroke="#CCCCCC" stroke-width="0.04"></g><g id="SVGRepo_iconCarrier"><path d="M17 9a1 1 0 01-1-1c0-.551-.448-1-1-1H5.414l1.293 1.293a.999.999 0 11-1.414 1.414l-3-3a.999.999 0 010-1.414l3-3a.997.997 0 011.414 0 .999.999 0 010 1.414L5.414 5H15c1.654 0 3 1.346 3 3a1 1 0 01-1 1zM3 11a1 1 0 011 1c0 .551.448 1 1 1h9.586l-1.293-1.293a.999.999 0 111.414-1.414l3 3a.999.999 0 010 1.414l-3 3a.999.999 0 11-1.414-1.414L14.586 15H5c-1.654 0-3-1.346-3-3a1 1 0 011-1z" fill="#c4c4c4"></path></g></svg>
                    </div>
                    <div id="undo_btn" onClick={undoBoard} className="bg-[#302E2B] hover:bg-[#423f3b]  flex justify-center items-center py-2 rounded">
                        <svg width="32px" height="32px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#302E2B" stroke-width="0.00024000000000000003"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" clip-rule="evenodd" d="M7.53033 3.46967C7.82322 3.76256 7.82322 4.23744 7.53033 4.53033L5.81066 6.25H15C18.1756 6.25 20.75 8.82436 20.75 12C20.75 15.1756 18.1756 17.75 15 17.75H8.00001C7.58579 17.75 7.25001 17.4142 7.25001 17C7.25001 16.5858 7.58579 16.25 8.00001 16.25H15C17.3472 16.25 19.25 14.3472 19.25 12C19.25 9.65279 17.3472 7.75 15 7.75H5.81066L7.53033 9.46967C7.82322 9.76256 7.82322 10.2374 7.53033 10.5303C7.23744 10.8232 6.76256 10.8232 6.46967 10.5303L3.46967 7.53033C3.17678 7.23744 3.17678 6.76256 3.46967 6.46967L6.46967 3.46967C6.76256 3.17678 7.23744 3.17678 7.53033 3.46967Z" fill="#c4c4c4"></path> </g></svg>
                    </div>
                    <div id="suggest_btn" className="bg-[#302E2B] hover:bg-[#423f3b]  flex justify-center items-center py-2 rounded">
                        <svg width="35px" height="35px" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#c4c4c4" stroke-width="1.488"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g id="idea"> <g id="idea_2"> <path id="Combined Shape" fill-rule="evenodd" clip-rule="evenodd" d="M23 5V7C23 7.55228 23.4477 8 24 8C24.5523 8 25 7.55228 25 7V5C25 4.44772 24.5523 4 24 4C23.4477 4 23 4.44772 23 5ZM26.887 29.9786H21.123C19.4134 29.9786 18.005 31.3089 18.005 32.9786V41.3486C18.005 42.7823 19.2093 43.9206 20.669 43.9206H27.329C28.7887 43.9206 29.995 42.7823 29.995 41.3486L30.0019 35.5387C34.1757 33.3634 37.0002 28.9948 37.0002 24.0022C37.0002 16.8239 31.1785 11.0022 24.0002 11.0022C16.8206 11.0022 11.0002 16.8232 11.0002 24.0022C11.0002 27.1579 12.1289 30.1397 14.1464 32.4827C14.5068 32.9012 15.1382 32.9484 15.5567 32.588C15.9752 32.2276 16.0224 31.5962 15.662 31.1777C13.9541 29.1942 13.0002 26.6743 13.0002 24.0022C13.0002 17.9278 17.9252 13.0022 24.0002 13.0022C30.0739 13.0022 35.0002 17.9285 35.0002 24.0022C35.0002 27.846 33.0212 31.253 30.0047 33.2223L30.005 32.9818C30.005 31.3093 28.5971 29.9786 26.887 29.9786ZM28.0035 34.2527L28.005 32.9806C28.005 32.4399 27.517 31.9786 26.887 31.9786H21.123C20.4932 31.9786 20.005 32.4398 20.005 32.9786V41.3486C20.005 41.6517 20.2895 41.9206 20.669 41.9206H27.329C27.7092 41.9206 27.995 41.651 27.995 41.3474L28.0009 36.3762C27.0928 36.6692 26.1399 36.8655 25.154 36.9523C24.6038 37.0008 24.1185 36.5941 24.0701 36.044C24.0216 35.4938 24.4283 35.0085 24.9784 34.9601C26.0387 34.8666 27.0538 34.6236 28.0035 34.2527ZM41 23H43C43.5523 23 44 23.4477 44 24C44 24.5523 43.5523 25 43 25H41C40.4477 25 40 24.5523 40 24C40 23.4477 40.4477 23 41 23ZM7 23H5C4.44772 23 4 23.4477 4 24C4 24.5523 4.44772 25 5 25H7C7.55228 25 8 24.5523 8 24C8 23.4477 7.55228 23 7 23ZM10.0001 8.58589L11.4141 9.99989C11.8046 10.3904 11.8046 11.0236 11.4141 11.4141C11.0236 11.8046 10.3904 11.8046 9.99989 11.4141L8.58589 10.0001C8.19537 9.60958 8.19537 8.97642 8.58589 8.58589C8.97642 8.19537 9.60958 8.19537 10.0001 8.58589ZM38.0001 11.4141L39.4141 10.0001C39.8046 9.60958 39.8046 8.97642 39.4141 8.58589C39.0236 8.19537 38.3904 8.19537 37.9999 8.58589L36.5859 9.99989C36.1954 10.3904 36.1954 11.0236 36.5859 11.4141C36.9764 11.8046 37.6096 11.8046 38.0001 11.4141Z" fill="#c4c4c4"></path> </g> </g> </g></svg>
                    </div>
                </div>
            </div>
}

export default function ChessBoard() {
    const [game, setGame] = useState(new Chess());
    const [customSquareStyles, setCustomSquareStyles] = useState({})

    const resetBoard = () => {
        console.log("clicked")
        setGame(new Chess())
    }

    const updateBoard = () => {
        const newGame = new Chess();
        game.history().forEach(move => newGame.move(move));
        setGame(newGame)
        console.log(game.history())
    }

    const undoBoard = () => {
        game.undo()
        game.undo()
        updateBoard()
    }
    
    const makeAMove = (move) => {
        try {
            const result = game.move(move);
            if (result) {
                updateBoard()
            }
            return result;
        } catch (error) {
            game.undo();
        }
    };

    const onDragBegin = (piece, sourceSquare) => {
        const moves = game.moves({ square: sourceSquare, verbose: true });
        const newSquareStyles = moves.reduce((styles, move) => {
            styles[move.to] = { backgroundColor: 'rgba(0, 0, 255, 0.5)' };
            return styles;
        }, {});
        setCustomSquareStyles(newSquareStyles);
    };

    const onDragEnd = () => {
        setCustomSquareStyles({});
    };

    const DisplayHistory = () => {
        const chunkedHistory = [];
        const history = game.history()
        for (let i = 0; i < history.length; i += 2) {
            chunkedHistory.push(history.slice(i, i + 2));
        }

        return (
            <div>
                <h3 className="text-[#929292] mb-2">History</h3>
                {chunkedHistory.map((chunk, index) => (
                    index % 2 === 0 ? (
                        <div className="grid grid-cols-[30px_60px_60px] py-1">
                            <span className="text-[#929292]">{index + 1}.</span>
                            {chunk.map((move, i) => (
                                <span className="font-semibold text-[#d6d5d5]">{move} </span>
                            ))}
                        </div>
                    ) : (  
                        <div className="grid grid-cols-[30px_60px_60px] py-1 px-2 bg-[#282724] mx-[-8px]">
                            <span className="text-[#929292]">{index + 1}.</span>
                            {chunk.map((move, i) => (
                                <span className="font-semibold text-[#d6d5d5]">{move} </span>
                            ))}
                        </div>
                    )
                ))}
            </div>
        );
    } 

    const onDrop = async (sourceSquare, targetSquare, piece) => {
        const move = makeAMove({
            from: sourceSquare,
            to: targetSquare,
            promotion: "q" 
        });

        if (!move) return false;

        try {
            const response = await fetch('http://localhost:5000/alphabeta', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ fen: game.fen() })
            });

            if (!response.ok) throw new Error('Network response was not ok.');

            const data = await response.json();
            game.move(data.best_move);
            updateBoard()
        } catch (error) {
            console.error("Failed to fetch the best move:", error);
        }

        return true;
    };



    return (
        <div className="grid grid-cols-[500px_350px] gap-10 w-fit ">
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
            <ControlPanel resetBoard={resetBoard} undoBoard={undoBoard} DisplayHistory={DisplayHistory}/>
            
        </div>      
    );
    }
