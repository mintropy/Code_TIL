import "./App.css";
import { useRef, useState, useEffect, useMemo } from "react";
import DiaryEditor from "./DiaryEditor";
import DiaryList from "./DiaryList";

function App() {
  const [data, setData] = useState([]);

  const dateId = useRef(0);

  const getDate = async () => {
    const res = await fetch(
      "https://jsonplaceholder.typicode.com/comments"
    ).then((res) => res.json());
    const initData = res.slice(0, 20).map((it) => {
      return {
        author: it.email,
        content: it.body,
        emotion: Math.floor(Math.random() * 5) + 1,
        created_date: new Date().getTime(),
        id: dateId.current++,
      };
    });
    setData(initData);
  };

  useEffect(() => {
    getDate();
  }, []);

  const onCreate = (author, content, emotion) => {
    const created_date = new Date().getTime();
    const newItem = {
      author,
      content,
      emotion,
      created_date,
      id: dateId.current,
    };
    dateId.current += 1;
    setData([newItem, ...data]);
  };

  const onRemove = (targetId) => {
    console.log(targetId);
    const newDiaryList = data.filter((item) => item.id !== targetId);
    setData(newDiaryList);
  };

  const onEdit = (targetId, newContent) => {
    setData(
      data.map((item) =>
        item.id === targetId ? { ...item, content: newContent } : item
      )
    );
  };

  const getDiaryAnalysis = useMemo(() => {
    console.log("일기 분석 시작");
    const goodCount = data.filter((it) => it.emotion >= 3).length;
    const badCount = data.length - goodCount;
    const goodRatio = (goodCount / data.length) * 100;
    return { goodCount, badCount, goodRatio };
  }, [data.length]);

  const { goodCount, badCount, goodRatio } = getDiaryAnalysis;

  return (
    <div className="App">
      <DiaryEditor onCreate={onCreate} />
      <div>전체 일기 : {data.length}</div>
      <div>기분 좋은 일기 : {goodCount}</div>
      <div>기분 나쁜 일기 : {badCount}</div>
      <div>기분 좋은 일기 비율 {goodRatio}</div>
      <DiaryList onRemove={onRemove} onEdit={onEdit} diaryList={data} />
    </div>
  );
}

export default App;
