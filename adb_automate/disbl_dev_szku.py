import time
import rich
from rich import progress
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn, track
from rich.prompt import Prompt
from rich.table import Column
from rich.text import Text
from rich.markdown import Markdown
from functionality.adb import ADB_COMMANDS, list_devices
from install_drivers import PACKAGES, check_installed, install_package
from functionality.command_runner import github_release_download, run_adb
from functionality.mods_list_src import Shizuku_MODS, Flashable_MODS
from functionality.mods import activate_shizuku

console = Console()


def install_drivers():
    """
    # Checking for Drivers and Necessary components
    """
    for name, package in PACKAGES.items():
        if check_installed(package):
            rich.print("ok")
        else:
            install_package(package)


# def connect_device():
#     has_device = False
#     while not has_device:
#         output = list_devices()
#         if "device" in output:
#             has_device = True


def connect_device():
    has_device = False
    while not has_device:
        output = list_devices()
        yield f"{output}"  # Yield the current output for live updates

        if "devicerrt" in output:
            has_device = True

    yield "Device connected."


def main():
    """
    Connect your Android Phone
    Goto Developer Optiones -> enable "USB Debugging"
    Click allow in the popup window (always allow)
    """

    """
    Would You like to Proceed The Setup?
    """

    for pkg in ["Shizuku", "Geto", "aShellYou"]:
        d_path = github_release_download(Flashable_MODS[pkg]["src"])
        out = run_adb("install", d_path)
        if out != 0:
            run_adb("push", d_path, "/sdcard/Downloads")

    activate_shizuku()


if __name__ == "__main__":
    # install_drivers()
    # connect_device()
    # main()

    m = Markdown(
        """
    
# Initial Preperation  

Connect your Android Phone  
Goto Developer Optiones -> enable "USB Debugging"  
Click allow in the popup window (always allow)  
    """
    )

p = Panel(
    m,
)
console.print(p)

c = Prompt.ask("Would you like to proceed", choices=["y", "n"])
# console.print(Panel(Prompt.ask("Would you like to proceed", choices=["y", "n"])))


generator = connect_device()
connect_device()
with Live(console=console, refresh_per_second=4) as live:
    for message in generator:
        # Each iteration updates the Live display
        live.update(message)
with Progress("package"):
    for n in progress.track(sequence=range(100), description="jh"):
        # progress.print(n)
        time.sleep(0.1)

# with Progress(connect_device()):
