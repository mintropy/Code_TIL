import { useState } from "react";
import "./App.css";
import Main from "./MainComponent";
import Sub from "./SubComponent";
import Modal from "./Modal";

function App() {
  const [num, setNum] = useState<number>(0);
  const [modalOpen, setModalOpen] = useState<boolean>(false);

  return (
    <div>
      <header>React</header>
      <Main num={num} />
      <Sub num={num} setNum={setNum} />
      <hr />
      {/* <div>num: {num}</div> */}
      {/* <button onClick={() => setNum(num + 1)}>+1</button>
      <button onClick={() => setNum(num - 1)}>-1</button> */}
      <div>
        <h3>Modal</h3>
        <button onClick={() => setModalOpen(true)}>Open</button>
        {modalOpen && (
          <Modal open={modalOpen} onClose={() => setModalOpen(false)}>
            <h4>Modal Content</h4>
            <div>num: {num}</div>
            <button onClick={() => setModalOpen(false)}>Close</button>
          </Modal>
        )}
      </div>
    </div>
  );
}

export default App;
