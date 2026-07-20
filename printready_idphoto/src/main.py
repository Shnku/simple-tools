import time

import flet as ft
from PIL import Image

from utils.img_resize import choose_size_options, resize_with
from utils.make_imgrid import border_photo, create_grid

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
    save_picker = ft.FilePicker()
    selected_img = ft.Image(src="icon.png", height=400, width=400)
    output_img = ft.Image(src="icon.png", height=400, width=400)
    dropdown = ft.Dropdown(
        options=[ft.DropdownOption(key=size, text=size) for size in size_list],
    )
    files: list[ft.FilePickerFile]
    grid_image = None
    save_location = ""

    # =====Clicking on Converter=========
    async def handle_button_click(_: ft.Event[ft.Button]):
        nonlocal grid_image
        print("dropdown value:", dropdown.value or "None")
        if files:
            with Image.open(str(selected_img.src)) as photo:
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
                name = f"demo_grid_a4_{time.time()}.png"
                grid.save(name)
                output_img.src = name
                print("GUI: new image grid created........")
                grid_image = grid
                output_img.update()

    # ==========select file=====
    async def handle_pick_files(e: ft.Event[ft.Button]):
        nonlocal files
        print("GUI : Clicked on convert..............")
        files = await picker.pick_files(
            file_type=ft.FilePickerFileType.IMAGE,
        )
        if files:
            selected_files.value = files[0].name
            selected_img.src = f"{files[0].path}"
            selected_img.update()

    # ==========opens file dialog to choose save location=====
    async def handle_save_file(e):
        try:
            save_location = await save_picker.save_file(
                "choose tee location",
                file_name="output_grid.png",
                file_type=ft.FilePickerFileType.IMAGE,
            )
            if not save_location:
                return
            print("save_file location--->>>", save_location)
            grid_image.save(str(save_location))
            page.update()
        except e:
            print("error saving ", e)

    # ================================================================== #
    #                               GUI PART                             #
    # ================================================================== #
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        title=ft.Text("ID Photo Converter"),
        center_title=True,
    )
    page.add(
        ft.Row(
            wrap=True,
            controls=[
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Button(
                            content="Pick files",
                            icon=ft.Icons.UPLOAD_FILE,
                            on_click=handle_pick_files,
                        ),
                        selected_files,
                        ft.Card(
                            ft.InteractiveViewer(
                                content=selected_img,
                                boundary_margin=3,
                            ),
                        ),
                    ],
                ),
                ft.Container(
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            dropdown,
                            ft.Button(
                                content="Convert",
                                icon=ft.Icons.TRANSFORM,
                                on_click=handle_button_click,
                            ),
                        ],
                    ),
                    width=400,
                ),
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Card(
                            ft.InteractiveViewer(
                                content=output_img,
                                constrained=True,
                            ),
                        ),
                        ft.Button(
                            content="Save to Custom Location",
                            icon=ft.Icons.FOLDER_OPEN,
                            on_click=handle_save_file,
                        ),
                        ft.Text(
                            f"The file is Saved at {save_location}",
                        ),
                    ],
                ),
            ],
        )
    )


if __name__ == "__main__":
    ft.run(main, assets_dir="assets", upload_dir="assets/uploads")
