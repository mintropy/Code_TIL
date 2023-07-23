import Backdrop from "./components/Backdrop";
import Modal from "./components/Modal";
import Todo from "./components/Todo";

function App() {
  return (
    <div>
      <h1>Todos</h1>
      <Todo title="make todo list" />
      <Todo title="publish todo list" />
      <Todo title="my own todo list" />
      <Modal />
      <Backdrop />
    </div>
  );
}

export default App;
