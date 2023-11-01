export default function Layout({
  children,
  parallel,
}: {
  children: React.ReactNode;
  parallel?: boolean;
}) {
  return (
    <>
      <div className="box">Intercepting I</div>
      {children}
      {parallel}
    </>
  );
}
