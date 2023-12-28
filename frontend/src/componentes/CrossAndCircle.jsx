import React, { useState } from "react";
import '../App.css';


export default function Game() {

  const [xIsNext, setxIsNext] = useState(false);
  const [errors, setErrors] = useState(false);


  const handleSubmit = async (index) => {
    try {
      const response = await api.get(`/api/words/findWord?original=${index}`);
      console.log(response);
    } catch (error) {
      if (error.response && error.response.data && error.response.data.errors) {
        setErrors(error.response.data.errors);
        console.log(errors);
      }
    }
  };

  
  const onClick = (index) => {
    setxIsNext(!xIsNext);
    console.log(index + 1);
    handleSubmit(index);
  };

  return (
    <div className="board">
      {[...Array(9).keys()].map((index) => (
        <button
          key={index}
          className={`square squares`}
          onClick={() => onClick(index)}
        >
        </button>
      ))}
    </div>
  );
};
