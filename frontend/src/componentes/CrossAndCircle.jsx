import React, { useState, useEffect } from "react";
import axios from "axios";
import '../App.css';

export default function Game() {
  const [xIsNext, setxIsNext] = useState(false);
  const [errors, setErrors] = useState(false);
  const [squares, setSquares] = useState(Array(9).fill("")); // Array to store values for each square
  const [vsAI, setVsAI] = useState(false);
  const [calculateWinner, setCalculateWinner] = useState(false);
  const [count, setCount] = useState(1);

  const handleSubmit = async (newSquares) => {
    const data = {
      squares: newSquares,
      vsAI: vsAI
    };

    try {
      const response = await axios.post("https://tic-tac-toe-server-m4ks.onrender.com", data);//http://127.0.0.1:5001/api/data
      const win = response.data.win
      const squaresFlat = response.data.squares.flat()
      if (win) {
        setSquares(squaresFlat);
        alert(`win is: ${win}`);
        location.reload();
      }

      setSquares(squaresFlat);

      console.log(squares);
    } catch (error) {
      if (error.response && error.response.data && error.response.data.errors) {
        setErrors(error.response.data.errors);
        console.log(errors);
      }
    }
  };

  const onClick = (index) => {

    if (vsAI) {
      // Check if the square is already filled or the game is over
      if (squares[index] || calculateWinner) {
        return;
      }

      setxIsNext(!xIsNext);

      // Clone the squares array to avoid mutating state directly
      const newSquares = [...squares];

      if (vsAI === 2) {
        // Update the value for the clicked square based on xIsNext
        newSquares[index] = "X";
        // newSquares[index] = !xIsNext ? "X" : "O";
      }


      if (vsAI === 1) {
        if (count % 2 == 0) {
          newSquares[index] = "O";
        } else {
          newSquares[index] = "X";
        }
      }

      setCount(count+1)
      // Update the state with the new squares array
      setSquares(newSquares);

      handleSubmit(newSquares, vsAI);
    }
  };



  return (
    <div className="board">
      {squares.map((value, index) => (
        <button
          key={index}
          className={`square squares`}
          onClick={() => onClick(index)}
        >
          {value}
        </button>
      ))}
      {!vsAI && (
        <>
          <button onClick={() => setVsAI(1)}>לשחק נגד חבר</button>
          <button onClick={() => setVsAI(2)}>לשחק נגד המחשב</button>
        </>
      )}

    </div>
  );
};