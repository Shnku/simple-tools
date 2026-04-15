from PIL import Image, ImageOps

from utils.img_resize import resize_with
from utils.print_canvas_size import (
    getsize_a4_canvas,
    getsize_passport_2x2_inch,
    getsize_visa_35x45_mm,
    inches_to_pixels,
)


def border_photo(photo, border_inches=0.1, color="white"):
    return ImageOps.expand(
        photo,
        inches_to_pixels(border_inches),
        color,
    )


def create_grid(photos_list, margin=0.5, ppi=300):
    print(photos_list[0])
    a4_size = getsize_a4_canvas(ppi=ppi)
    canvas = Image.new("RGB", size=a4_size, color="white")
    margin_start = inches_to_pixels(margin, ppi=ppi)
    pos_x, pos_y = margin_start, margin_start
    for pic in photos_list:
        if pos_x + pic.width >= a4_size[0] - margin_start:
            pos_x, pos_y = margin_start, pos_y + pic.height
            if pos_y + pic.height >= a4_size[1] - margin_start:
                print("less printed as page overflow")
                break
        canvas.paste(pic, (int(pos_x), int(pos_y)))
        pos_x += pic.width
    canvas.show()
    return canvas


def main():
    with Image.open("../assets/icon.png") as photo:
        photo = resize_with(
            photo,
            getsize_passport_2x2_inch(ppi=300),
        )
        photo2 = resize_with(
            photo,
            getsize_visa_35x45_mm(ppi=300),
        )
        photo = border_photo(photo)
        photo2 = border_photo(photo2)
        list_of_pics = (
            [photo for _ in range(5)]
            + [photo2 for _ in range(5)]
            + [photo for _ in range(5)]
        )
        photo.show()
        photo2.show()
        print(photo)
        grid = create_grid(list_of_pics)
        # grid.show()
        grid.save("demo_grid_a4.jpg")


if __name__ == "__main__":
    main()
