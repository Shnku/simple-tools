import flet as ft
from PIL import Image, ImageOps
from utils.img_resize import choose_size_options
from utils.make_imgrid import create_grid, border_photo
from utils.img_resize import resize_with

size_list = [
    "Passport (2x2inch)",
    "OCI Passport (3.5x3.5cm)",
    "Visa (3.5x4.5cm)",
    "PAN Card (2.5x3.5cm)",
    "Stamp (2x2.5cm)",
]


def main(page: ft.Page):
    selected_files = ft.Text()
    picker = ft.FilePicker()
    selected_img = ft.Image(
        src="icon.png",
        height=400,
        width=400,
    )
    dropdown = ft.Dropdown(
        options=[ft.DropdownOption(key=size, text=size) for size in size_list],
    )

    def handle_button_click(_: ft.Event[ft.Button]):
        print("dropdown value:", dropdown.value or "None")

    async def handle_pick_files(e: ft.Event[ft.Button]):
        files = await picker.pick_files(
            with_data=False, allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE
        )
        if files:
            selected_files.value = files[0].name
            selected_img.src = f"{files[0].path}"
            with Image.open(str(files[0].path)) as photo:
                photo = resize_with(
                    photo,
                    choose_size_options(
                        PPI=300,
                        choice=size_list.index(dropdown.value) + 1
                        if dropdown.value
                        else 1,
                    ),
                )
                photo = border_photo(photo)
                list_of_pics = [photo for _ in range(10)]
                grid = create_grid(list_of_pics)
                grid.save("./demo_grid_a4.jpg")
                page.add(
                    ft.Column(
                        controls=[
                            ft.Text(
                                "Converted image saved as demo_grid_a4.jpg in project folder."
                            ),
                            ft.Image(src="./demo_grid_a4.jpg", height=400, width=400),
                        ]
                    )
                )
                selected_img.update()
        page.update()

    page.appbar = ft.AppBar(title=ft.Text("ID Photo Converter"))
    page.add(
        ft.Column(
            run_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Button(
                    content="Pick files",
                    icon=ft.Icons.UPLOAD_FILE,
                    on_click=handle_pick_files,
                ),
                selected_files,
                ft.InteractiveViewer(
                    content=selected_img,
                ),
                dropdown,
                ft.Button(
                    content="Convert",
                    icon=ft.Icons.TRANSFORM,
                    on_click=handle_button_click,
                ),
            ],
        )
    )


if __name__ == "__main__":
    ft.run(main, assets_dir="assets", upload_dir="assets/uploads")
