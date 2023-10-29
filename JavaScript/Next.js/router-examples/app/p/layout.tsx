export default function Layout(props: {
  children: React.ReactNode;
  q: React.ReactNode;
  r: React.ReactNode;
}) {
  return (
    <>
      <div className="box">parallel main</div>
      {props.children}
      {props.q}
      {props.r}
    </>
  );
}
