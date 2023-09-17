import Link from "next/link";
import { ReactNode } from "react";

export default function Modal({ children }: { children: ReactNode }) {
  return (
    <div>
      <Link href="/" className="modal" />
      {children}
    </div>
  );
}
