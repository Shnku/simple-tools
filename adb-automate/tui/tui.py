from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import (
    Footer,
    Header,
    Label,
    ListItem,
    ListView,
    RichLog,
    Static,
)

from adb_functionality import ADB_COMMANDS, adb_version, list_devices


class SideView(Container):
    BORDER_TITLE = "functions"

    def compose(self) -> ComposeResult:
        with ListView():
            for i in ADB_COMMANDS.keys():
                yield ListItem(Label(i))
        return super().compose()

    def on_mount(self):
        self.id = "sideview"
        self.classes = "box"


class MainView(Container):
    BORDER_TITLE = "Choose"

    def on_mount(self):
        self.id = "mainview"
        self.classes = "box"
        self.content = "hi"
        self.mount(Static(adb_version(), markup=True))


class Output(Container):
    BORDER_TITLE = "Output Log"

    def compose(self) -> ComposeResult:
        yield RichLog()
        return super().compose()

    def on_mount(self):
        self.id = "output"
        self.classes = "box"
        self.query_one(RichLog).write(list_devices())


class MainTUI(App):
    CSS_PATH = "tui.tcss"
    TITLE = "ADB Fastboot TUI"

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            with Horizontal():
                yield SideView()
                yield MainView()
            yield Output()
        yield Footer()

    def on_mount(self) -> None:
        self.query(Static).nodes[1].border_title = "functions"


if __name__ == "__main__":
    app: MainTUI = MainTUI()
    app.run()
