export default function Page({ params }: { params: { id: string } }) {
  return (
    <>
      <div className="box">id: {params.id}</div>
    </>
  );
}
