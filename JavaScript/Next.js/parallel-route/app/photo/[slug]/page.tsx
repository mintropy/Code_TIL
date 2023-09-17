import Image from "next/image";
import { imgUrls } from "@/data";
import Modal from "@/components/modal";

export default function Page({
  params: { slug },
}: {
  params: { slug: number };
}) {
  return (
    <Modal>
      <div className="photo_container">
        <Image
          src={imgUrls[slug]}
          alt={imgUrls[slug]}
          width={100}
          height={100}
          style={{ width: "100%", height: "100%", objectFit: "contain" }}
          sizes="60vw"
          priority
        />
      </div>
    </Modal>
  );
}
