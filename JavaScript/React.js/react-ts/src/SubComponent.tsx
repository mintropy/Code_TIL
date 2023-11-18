export default function Sub({
  num,
  setNum,
}: {
  num: number;
  setNum: React.Dispatch<React.SetStateAction<number>>;
}) {
  return (
    <div>
      <h2>Sub</h2>
      <button onClick={() => setNum(num + 1)}>+1</button>
      <button onClick={() => setNum(num - 1)}>-1</button>
    </div>
  );
}
