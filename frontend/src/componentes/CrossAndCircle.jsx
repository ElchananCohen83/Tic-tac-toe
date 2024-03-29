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

  useEffect(() => {
    if (calculateWinner) {
      // Delay the alert to allow the UI to update first
      const timeoutId = setTimeout(() => {
        alert(`Win is: ${calculateWinner}`);
        location.reload();
      }, 100);

      // Cleanup the timeout to avoid memory leaks
      return () => clearTimeout(timeoutId);
    }
  }, [calculateWinner]);

  const handleSubmit = async (newSquares) => {
    const data = {
      squares: newSquares,
      vsAI: vsAI
    };

    try {
      const response = await axios.post("https://tic-tac-toe-server-m4ks.onrender.com/api/data", data)
      // const response = await axios.post("http://127.0.0.1:5001/api/data", data);
      console.log(response.data);
      setCalculateWinner(response.data.win)
      const squaresFlat = response.data.squares.flat()

      if (calculateWinner) {
        alert(`win is: ${win}`);
        location.reload();
      }

      setSquares(squaresFlat);

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
        newSquares[index] = "X";
    }

    if (vsAI === 1) {
      if (count % 2 == 0) {
        newSquares[index] = "O";
      } else {
        newSquares[index] = "X";
      }
    }

    setCount(count + 1)
    // Update the state with the new squares array
    setSquares(newSquares);

    handleSubmit(newSquares, vsAI);

  }
};

  return (
    <div>
      {!vsAI && (
        <div className="req_vs">
          <h1>אני רוצה לשחק עם</h1>
          <div className="button">
            <button className="choose" onClick={() => setVsAI(1)}>חבר</button>
            <button className="choose" onClick={() => setVsAI(2)}>מחשב</button>
          </div>
        </div>
      )}
      
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
      </div>
    </div>
  );
};


// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import '../App.css';
// import CryptoJS from 'crypto-js';

// export default function Game() {
//   const [xIsNext, setxIsNext] = useState(false);
//   const [errors, setErrors] = useState(false);
//   const [squares, setSquares] = useState(Array(9).fill("")); // Array to store values for each square
//   const [vsAI, setVsAI] = useState(false);
//   const [calculateWinner, setCalculateWinner] = useState(false);
//   const [count, setCount] = useState(1);


//   // const backgroundImage = import.meta.env.VITE_BACKGROUND_IMAGE || 'url(./public/background.jpg)';

//   useEffect(() => {
//     if (calculateWinner) {
//       const timeoutId = setTimeout(() => {
//         alert(`Win is: ${calculateWinner}`);
//         location.reload();
//       }, 100);

//       return () => clearTimeout(timeoutId);
//     }
//   }, [calculateWinner]);

//   const handleSubmit = async (newSquares) => {
//     const data = {
//       squares: newSquares,
//       vsAI: vsAI
//     };

//     const encryptData = (data) => {
//       const secretKey =  import.meta.env.VITE_SECRET_KEY
//       const encryptedData = CryptoJS.AES.encrypt(JSON.stringify(data), secretKey).toString();
//       return {
//         data: encryptedData
//       };
//     };

//     console.log(12345, encryptData(data));

//     try {
//       const response = await axios.post("http://127.0.0.1:5001/api/data", encryptData(data));
//       setCalculateWinner(response.data.win);
//       setSquares(response.data.squares.flat());
//       if (calculateWinner) {
//         alert(`win is: ${win}`);
//         location.reload();
//       }

//       console.log(squares);
//     } catch (error) {
//       if (error.response && error.response.data && error.response.data.errors) {
//         setErrors(error.response.data.errors);
//         console.log(errors);
//       }
//     }
//   };

//   const onClick = (index) => {

//     if (vsAI) {
//       // Check if the square is already filled or the game is over
//       if (squares[index] || calculateWinner) {
//         return;
//       }

//       setxIsNext(!xIsNext);

//       // Clone the squares array to avoid mutating state directly
//       const newSquares = [...squares];

//       if (vsAI === 2) {
//         // Update the value for the clicked square based on xIsNext
//         newSquares[index] = "X";
//         // newSquares[index] = !xIsNext ? "X" : "O";
//       }


//       if (vsAI === 1) {
//         if (count % 2 == 0) {
//           newSquares[index] = "O";
//         } else {
//           newSquares[index] = "X";
//         }
//       }

//       setCount(count + 1)
//       // Update the state with the new squares array
//       setSquares(newSquares);

//       handleSubmit(newSquares, vsAI);
//     }
//   };

//   return (
//     <div>
//       {!vsAI && (
//         <div className="req_vs">
//           <h1>אני רוצה לשחק עם</h1>
//           <div className="button">
//             <button className="choose" onClick={() => setVsAI(1)}>חבר</button>
//             <button className="choose" onClick={() => setVsAI(2)}>מחשב</button>
//           </div>
//         </div>
//       )}
      
//       <div className="board">
//         {squares.map((value, index) => (
//           <button
//             key={index}
//             className={`square squares`}
//             onClick={() => onClick(index)}
//           >
//             {value}
//           </button>
//         ))}
//       </div>
//     </div>
//   );
// };