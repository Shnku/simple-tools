import flet as ft

from mainpage import DownloaderApp


def main(page: ft.Page):
    page.title = "Downloader App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.update()

    app = DownloaderApp()
    page.add(
        ft.Container(
            expand=True,
            content=app,
            margin=ft.margin.all(20),
        )
    )


ft.run(main)
