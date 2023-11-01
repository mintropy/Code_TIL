import { Inter } from "next/font/google";
import "./globals.css";
import Link from "next/link";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <>
        <body className={inter.className}>
          <h1>Router Examples</h1>
          <Link href="/">Home</Link>
          <br />
          <b>Basic Routings </b>
          <Link href="/a">A</Link>
          --
          <Link href="/a/b">B</Link>
          <br />
          <b>Dynamic Routings </b>
          {["a", "b", "c", "d"].map((id, idx) => (
            <span key={idx}>
              <Link href={`/d/${id}`}>d-{id}</Link>
              <span> </span>
            </span>
          ))}
          <br />
          <b>Parallel Routings </b>
          <Link href="/p">p</Link>
          <br />
          <b>Intercepting Routings </b>
          <Link href="/i">i</Link>
          <hr />
          <div className="box">Main</div>
          {children}
        </body>
      </>
    </html>
  );
}
