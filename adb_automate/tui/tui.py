from textual import on
from functionality.adb import ADB_COMMANDS, adb_version, list_devices

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


class SideView(Container):
    BORDER_TITLE = "functions"
    selected_item = ""

    def compose(self) -> ComposeResult:
        with ListView(id="adb-list"):
            for name, subitem in ADB_COMMANDS.items():
                yield ListItem(Label(name))

    def on_mount(self):
        self.classes = "box"

    @on(ListView.Selected, "#adb-list")
    def on_list_selected(self, event: ListView.Selected):
        index: int | None = event.list_view.index
        if index is None:
            return
        self.selected_item = list(ADB_COMMANDS.keys())[index]


class MainView(Container):
    BORDER_TITLE = "Choose"

    def on_mount(self):
        self.classes = "box"
        self.mount(Static(adb_version(), markup=True))

    def custom(self, out):
        return Static(out)


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
                yield SideView(id="sideview")
                yield MainView(id="mainview")
            yield Output()
        yield Footer()

    @on(ListView.Selected)
    def on_list_selected(self, event: ListView.Selected):
        self.selected_item = event.item
        self.run_worker(self.subitem_selection, exclusive=True)

    async def subitem_selection(self):
        item = self.query_one(SideView).selected_item
        self.query_one("#mainview").mount(Static(str(ADB_COMMANDS.get(item))))
        return item

    async def update_output(self):
        item = self.query_one(SideView).selected_item
        out = ADB_COMMANDS[item]()
        return out
        # pass


if __name__ == "__main__":
    app: MainTUI = MainTUI()
    app.run()
