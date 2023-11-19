import { useState } from "react";
import "./App.css";
import Main from "./MainComponent";
import Sub from "./SubComponent";
import Modal from "./Modal";
import { BrowserRouter, Route, Link, Routes } from "react-router-dom";

function App() {
  const [num, setNum] = useState<number>(0);
  const [modalOpen, setModalOpen] = useState<boolean>(false);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<div>Home</div>} />
        <Route path="/about" element={<div>About</div>} />
        <Route path="/users" element={<div>Users</div>} />
        <Route path="/users/:id" element={<div>Users/:id</div>} />
        {/* <Route path="/articles" element={<div>Articles</div>}>
          <Route path="/" element={<div>Articles</div>} />
          <Route path="/:id" element={<div>Articles/:id</div>} />
        </Route> */}
      </Routes>
      <div>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/users">Users</Link>
        <Link to="/users/1">Users/1</Link>
        <Link to="/articles">Articles</Link>
        <Link to="/articles/1">Articles/1</Link>
      </div>
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
    </BrowserRouter>
  );
}

export default App;
