import { imgUrls } from "@/data";
import Image from "next/image";
import Link from "next/link";

export default function Page() {
  return (
    <div className="gallery">
      {imgUrls.map((url, index) => (
        <Link key={index} href={`/photo/${index}`}>
          <Image
            src={url}
            alt={url}
            width={100}
            height={100}
            style={{ width: "100%", height: "100%", objectFit: "contain" }}
            sizes="60vw"
            priority
          />
        </Link>
      ))}
    </div>
  );
}
