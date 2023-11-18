import { useState } from "react";
import "./App.css";
import Main from "./MainComponent";
import Sub from "./SubComponent";

function App() {
  const [num, setNum] = useState<number>(0);

  return (
    <div>
      <header>React</header>
      <Main num={num} />
      <Sub num={num} setNum={setNum} />
      <hr />
      {/* <div>num: {num}</div> */}
      {/* <button onClick={() => setNum(num + 1)}>+1</button>
      <button onClick={() => setNum(num - 1)}>-1</button> */}
    </div>
  );
}

export default App;
