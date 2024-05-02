import ChessBoard from "./component/Main";
import Header from "./component/header/header";

function App() {
  return (
    <div className="App bg-[#302E2B] h-[100vh] pt-5 pl-5">
        <Header/>;
        <div className="flex justify-center items-center">
            <div>
                <ChessBoard/>
            </div>
        </div>
    </div>
  );
};

export default App;
