import flet as ft


@ft.control
class DownloaderApp(ft.Column):
    # application's root control is a Column containing all other controls
    def init(self):
        self.put_url = ft.TextField(
            label="Enter the URL Link: ",
            expand=True,
            on_submit=self.add_clicked,
            adaptive=True,
            border=ft.InputBorder.OUTLINE,
            border_color=ft.Colors.BLUE,
            border_radius=20,
        )
        self.tasks_view = (
            ft.GridView(
                adaptive=True,
                auto_scroll=True,
                expand_loose=True,
                align=ft.Alignment.CENTER,
            ),
        )
        self.width = 600
        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        self.run_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            self.put_url,
            ft.FloatingActionButton(
                icon=ft.Icons.GET_APP,
                expand=True,
                on_click=self.add_clicked,
            ),
            ft.Container(
                expand=True,
                content=self.tasks_view[0],
            ),
        ]

    def add_clicked(self, e):
        self.tasks_view[0].controls.append(ft.Checkbox(label=self.put_url.value))
        self.put_url.value = ""
        self.update()
