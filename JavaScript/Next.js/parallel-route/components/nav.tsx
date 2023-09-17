import Link from "next/link";

export default function Nav() {
  return (
    <nav>
      <Link href="/auth/login">Login</Link>
      <Link href="/auth/register">Register</Link>
    </nav>
  );
}
