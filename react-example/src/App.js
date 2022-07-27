// import "./App.css";

import MyHeader from "./MyHeader";
import Counter from "./Counter";

function App() {
  const counterPorps = {
    a: 1,
    b: 2,
    c: 3,
    // initialValue: 5,
  };

  return (
    <div>
      <MyHeader />
      <Counter {...counterPorps} />
    </div>
  );
}

export default App;
