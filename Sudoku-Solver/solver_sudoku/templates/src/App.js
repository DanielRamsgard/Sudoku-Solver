import './App.css';
import { useState,useRef } from 'react'

const array = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1]
  ];

function App() {
    const [sudokuArr, setSudokuArr] = useState(getDeepCopy(array));
    const [isSolved, setIsSolved] = useState(false);
    const [getSolved, setGetSolved] = useState(false);
    const cellRefs = useRef({});

    function checkSolve(grid){
        for (let i = 0; i < 9; i++){
            if (grid[i].includes(-1)){
                setIsSolved(false);
            }
            if (i === 8 && !(grid[i].includes(-1))){
                setIsSolved(true);
            }
        }
    }

    function getDeepCopy(arr) {
        return JSON.parse(JSON.stringify(arr));
    }

    function handleKeyStroke(e, row, col) {
        if (e.key === "ArrowUp" && row > 0){
            const cell = cellRefs.current[`${row-1}-${col}`];
            setTimeout(() => {
                cell.focus();
                cell.setSelectionRange(cell.value.length, cell.value.length);
              }, 0);
        }
        else if (e.key === "ArrowDown" && row < 8){
            const cell = cellRefs.current[`${row+1}-${col}`];
            setTimeout(() => {
                cell.focus();
                cell.setSelectionRange(cell.value.length, cell.value.length);
              }, 0);
        }
        else if (e.key === "ArrowRight" && col < 8){
            const cell = cellRefs.current[`${row}-${col+1}`];
            setTimeout(() => {
                cell.focus();
                cell.setSelectionRange(cell.value.length, cell.value.length);
              }, 0);
        }
        else if (e.key === "ArrowLeft" && col > 0){
            const cell = cellRefs.current[`${row}-${col-1}`];
            setTimeout(() => {
                cell.focus();
                cell.setSelectionRange(cell.value.length, cell.value.length);
              }, 0);
        }
    }

    function onInputChange(e, row, col) {
        var val = parseInt(e.target.value) || -1;
        var grid = getDeepCopy(sudokuArr);
        handleKeyStroke(e, row, col);
        
        if (val === -1 || val >= 1 && val <= 9){
            let flag = true;
            if (!(sudokuArr[row].includes(val)) || val === -1){
                for (let i = 0; i < 9; i++){
                    if (sudokuArr[i][col] === val && val !== -1){
                        flag = false;
                    }
                }
                
                // upper left
                if (row % 3 === 0 && col % 3 === 0) {
                    if (sudokuArr[row+1][col+1] === val || sudokuArr[row+1][col+2] === val || sudokuArr[row+2][col+1] === val || sudokuArr[row+2][col+2] === val) {
                        if (val !== -1){
                            flag = false;
                        }
                    }
                }

                // upper middle
                if (row % 3 === 0 && col % 3 === 1) {
                    if (sudokuArr[row+1][col-1] === val || sudokuArr[row+1][col+1] === val || sudokuArr[row+2][col-1] === val || sudokuArr[row+2][col+1] === val) {
                        if (val !== -1){
                            flag = false;
                        }
                    }
                }

                // upper right
                if (row % 3 === 0 && col % 3 === 2) {
                    if (sudokuArr[row+1][col-2] === val || sudokuArr[row+1][col-1] === val || sudokuArr[row+2][col-2] === val || sudokuArr[row+2][col-1] === val) {
                        if (val !== -1){
                            flag = false;
                        }
                    }
                }

                // middle  left
                if (row % 3 === 1 && col % 3 === 0) {
                    if (sudokuArr[row-1][col+1] === val || sudokuArr[row-1][col+2] === val || sudokuArr[row+1][col+1] === val || sudokuArr[row+1][col+2] === val) {
                        if (val !== -1){
                            flag = false;
                        }
                    }
                }

                // middle middle
                if (row % 3 === 1 && col % 3 === 1) {
                    if (sudokuArr[row-1][col-1] === val || sudokuArr[row-1][col+1] === val || sudokuArr[row+1][col-1] === val || sudokuArr[row+1][col+1] === val) {
                        if (val !== -1){
                            flag = false;
                        }
                    }
                }

                // middle right
                if (row % 3 === 1 && col % 3 === 2) {
                    if (sudokuArr[row-1][col-2] === val || sudokuArr[row-1][col-1] === val || sudokuArr[row+1][col-2] === val || sudokuArr[row+1][col-1] === val) {
                        if (val !== -1){
                            flag = false;
                        }
                    }
                }

                // lower left
                if (row % 3 === 2 && col % 3 === 0) {
                    if (sudokuArr[row-2][col+1] === val || sudokuArr[row-2][col+2] === val || sudokuArr[row-1][col+1] === val || sudokuArr[row-1][col+2] === val) {
                        if (val !== -1){
                            flag = false;
                        }
                    }
                }

                // lower middle
                if (row % 3 === 2 && col % 3 === 1) {
                    if (sudokuArr[row-1][col-1] === val || sudokuArr[row-1][col+1] === val || sudokuArr[row-2][col-1] === val || sudokuArr[row-2][col+1] === val) {
                        if (val !== -1){
                            flag = false;
                        }
                    }
                }
                
                // lower right
                if (row % 3 === 2 && col % 3 === 2) {
                    if (sudokuArr[row-1][col-2] === val || sudokuArr[row-1][col-1] === val || sudokuArr[row-2][col-2] === val || sudokuArr[row-2][col-1] === val) {
                        if (val !== -1){
                            flag = false;
                        }
                    }
                }

                if (val === -1) {
                    grid[row][col] = val;
                }
                else if (flag){
                    grid[row][col] = val;
                }
            }


        }

        setSudokuArr(grid);
        checkSolve(grid);
    }

    const handleSolve = async () => {
        try {
            const response = await fetch('http://54.225.36.165/solver/solve/', {
                method: 'POST',
                body: JSON.stringify({'array': sudokuArr})
            });

            if (!response.ok) {
                return;
            }
            else {
                const data = await response.json();
                if (data.ret) {
                    setIsSolved(true);
                    setGetSolved(false);
                    setSudokuArr(data.board);
                } else {
                    setGetSolved(false);
                    setIsSolved(false);
                    setSudokuArr(data.board);
                }
            }

        } catch (error) {
            console.log(error);
        };

    }

    function getClassName(){
        if (getSolved){
            return "tableFalseFalse";
        } else {
            if (isSolved) {
                return "tableTrue";
            } else {
                return "tableFalse";
            }
        }
    }

    return (
    <div className="App">
        <header className="App-header">
            <h3 className="header"> Sudoku Solver </h3>
            <table className={getClassName()}>
                <tbody>
                    {
                    [0, 1, 2, 3, 4, 5, 6, 7, 8].map((row, rIndex) => {
                        return  <tr key={rIndex} className={(row + 1)% 3 === 0 ? "bBorder" : ''}>
                                {[0, 1, 2, 3, 4, 5, 6, 7, 8].map((col, cIndex) => {
                                    return  <td key={rIndex + cIndex} className={(col + 1)% 3 === 0 ? "rBorder" : ''}>
                                                <input 
                                                onChange={(e) => onInputChange(e, row, col)} 
                                                onKeyDown={(e) => handleKeyStroke(e, row, col)}
                                                value={sudokuArr[row][col] === -1 ? '' : sudokuArr[row][col]} 
                                                className={sudokuArr[row][col] === -1 ? "cellInput" : "cellInputted"}
                                                disabled={array[row][col] !== -1}
                                                ref={(el) => {cellRefs.current[`${row}-${col}`] = el}}
                                                />
                                    </td>
                                })}
                                </tr>
                    })
                    }
                </tbody>
            </table>
            <div className="buttonContainer flex space-x-4">
                <button className="solveButton" onClick={handleSolve}> Solve </button>
                <button className="resetButton" onClick={() => {setIsSolved(false); setSudokuArr(array)}}> Reset </button>
            </div>
        </header>
    </div>
    );
}

export default App;
