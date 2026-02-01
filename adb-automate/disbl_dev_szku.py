import rich
from rich.console import Console
from rich.panel import Panel
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


def connect_device():
    has_device = False
    while not has_device:
        output = list_devices()
        if "device" in output:
            has_device = True


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
    install_drivers()
    connect_device()
    main()
