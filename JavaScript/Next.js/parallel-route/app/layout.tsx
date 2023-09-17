import Nav from "@/components/nav";
import "./globals.css";

export default function RootLayout(props: any) {
  return (
    <html lang="en">
      <body>
        <Nav />
        <main>
          {props.children}
          {props.modal}
        </main>
      </body>
    </html>
  );
}
