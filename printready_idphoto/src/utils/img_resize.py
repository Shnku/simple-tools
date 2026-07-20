from PIL import Image

from utils.print_canvas_size import (
    getsize_oci_passport_35x35_mm,
    getsize_pan_25x35_mm,
    getsize_passport_2x2_inch,
    getsize_stamp_20x25_mm,
    getsize_visa_35x45_mm,
)


def resize_equally_factor(img: Image.Image, resize_factor=0.5, rev=True):
    print("original:", img)
    width, height = img.size
    if rev:
        resize_factor = 1 - resize_factor
    img = img.resize(
        (int(width * resize_factor), int(height * resize_factor)),
        Image.Resampling.LANCZOS,
    )
    print("resized:", img)
    return img


def resize_with(img: Image.Image, template_size: tuple[float, float]):
    to_width, to_height = template_size
    scale_w = to_width / img.width
    scale_h = to_height / img.height
    print("scaling:", scale_w, scale_h)
    scaling_factor = min(scale_w, scale_h)
    img = resize_equally_factor(img, scaling_factor, rev=False)
    return img


def choose_size_options(PPI, cli=False, choice=None):
    choice = choice
    if cli:
        choice = int(
            input("""   What to Convert? ...................
            1) Indian Passport Photo: 2 x 2 inch.
            2) Indian OCI (Overseas Citizenship of India): 3.5 x 3.5 cm.
            3) Indian Visa Photo: 3.5 x 4.5 cm.
            4) Indian PAN Card Photo: 2.5 x 3.5 cm.
            5) Indian Stamp Size Photo: 2 x 2.5 cm.
        Enter the format of your id photo:- """)
        )
    to_size = (0, 0)
    match choice:
        case 1:
            to_size = getsize_passport_2x2_inch(PPI)
        case 2:
            to_size = getsize_oci_passport_35x35_mm(PPI)
        case 3:
            to_size = getsize_visa_35x45_mm(PPI)
        case 4:
            to_size = getsize_pan_25x35_mm(PPI)
        case 5:
            to_size = getsize_stamp_20x25_mm(PPI)
        case _:
            print("Invalid choice. Defaulting to Passport Photo size.")
            to_size = getsize_passport_2x2_inch(PPI)
    return to_size


def main():
    PPI = 300
    path = "./demo_resized.jpg"

    with Image.open(path) as pic:
        # pic = resize_equally_factor(pic)
        pic = resize_with(pic, choose_size_options(PPI))
        pic.show()
        pic.save("demo_resized.jpg")


if __name__ == "__main__":
    main()
