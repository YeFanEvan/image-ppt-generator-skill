from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
from pathlib import Path
import argparse


def merge_images_to_pdf(image_paths, output_path):
    image_paths = [Path(p) for p in image_paths]
    if not image_paths:
        raise ValueError("No image paths provided.")
    for p in image_paths:
        if not p.exists():
            raise FileNotFoundError(p)

    first = Image.open(image_paths[0])
    c = canvas.Canvas(str(output_path), pagesize=first.size)

    for p in image_paths:
        img = Image.open(p)
        iw, ih = img.size
        c.setPageSize((iw, ih))
        c.drawImage(ImageReader(img), 0, 0, width=iw, height=ih)
        c.showPage()

    c.save()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge PPT page images into a PDF.")
    parser.add_argument("output", help="Output PDF path")
    parser.add_argument("images", nargs="+", help="Image paths in final order")
    args = parser.parse_args()
    merge_images_to_pdf(args.images, args.output)
