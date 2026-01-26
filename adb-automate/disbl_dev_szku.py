import rich
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from functionality.adb import list_devices
from install_drivers import PACKAGES, check_installed, install_package

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


if __name__ == "__main__":
    install_drivers()
    connect_device()
    main()
