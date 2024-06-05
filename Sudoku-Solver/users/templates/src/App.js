import './App.css';

function App() {
  return (
    <div className="Container">
        <div className="ImgDiv">
            <img className="Img" src="./static/media/sudoku.png"></img>
            <div className="TitleText">
                <p className="Title"> Sudoku Solver </p>
            </div>
        </div>
        <div className="Bar">
        </div>
        <div className="App">
            <div>
                <p className="TextWelcome"> Welcome to Sudoku Solver! </p>
            </div>
            <img className="Board" src="./static/media/sudoku.jpeg"></img>
            <div className="Play">
                <p className="TextPlay"> Please check out the project GitHub or play as guest. </p>
            </div>
            <div className="ButtonDiv">
                <a href="https://github.com/DanielRamsgard/Sudoku-Solver#readme" className="Button"> GitHub </a>
                <a href="solver/" className="Button"> Guest </a>
            </div>
        </div>
    </div>
  );
}

export default App;
