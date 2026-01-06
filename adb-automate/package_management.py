from typing import Any
from command_runner import run_adb


def search_app(app) -> list[Any]:
    found_list: list[Any] = []
    apps: str | Any = run_adb("shell", "pm", "list", "packages")
    # print(apps.splitlines())
    for i in apps.splitlines():
        if app in i:
            found_list.append(i)
    return found_list


def remove_app(apps) -> str | Any:
    return (run_adb("uninstall", app) for app in apps)


def install_app(apps) -> str | Any:
    print(f"apk:{apps} >>> ", end="")
    return run_adb("uninstall", apps)
