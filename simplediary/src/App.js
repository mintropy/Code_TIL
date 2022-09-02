import "./App.css";
import DiaryEditor from "./DiaryEditor";
import DiaryList from "./DiaryList";

const dummyList = [
  {
    id: 1,
    author: "mintropy",
    content: "Hello",
    emotion: 5,
    created_date: new Date().getTime(),
  },
  {
    id: 2,
    author: "mintropy",
    content: "Good Bye",
    emotion: 5,
    created_date: new Date().getTime(),
  },
];

function App() {
  return (
    <div className="App">
      <DiaryEditor />
      <DiaryList diaryList={dummyList} />
    </div>
  );
}

export default App;
