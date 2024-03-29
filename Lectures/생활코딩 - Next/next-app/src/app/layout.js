import Link from "next/link";
import "./globals.css";
import { Control } from "./Control";

export const metadata = {
  title: "Web tutorials",
  description: "Generated by mintropy",
};

export default async function RootLayout({ children }) {
  const resp = await fetch(process.env.NEXT_PUBLIC_API_URL + "/topics", {
    cache: "no-store",
  });
  const topics = await resp.json();
  return (
    <html>
      <body>
        <h1>
          <Link href="/">WEB</Link>
        </h1>
        <ol>
          {topics.map((topic) => {
            return (
              <li>
                <Link href={`/read/${topic.id}`} key={topic.id}>
                  {topic.title}
                </Link>
              </li>
            );
          })}
        </ol>
        {children}
        <Control />
      </body>
    </html>
  );
}
