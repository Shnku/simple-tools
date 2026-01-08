from typing import Any
from command_runner import run_adb


def list_devices() -> str | Any:
    return run_adb("devices")


def list_installed_apps() -> str | Any:
    return run_adb("shell", "pm", "list", "packages")


def search_app(app, apps_list) -> list[Any]:
    found_list: list[Any] = []
    for i in apps_list.splitlines():
        if app in i:
            found_list.append(i)
    return found_list


def remove_app(app) -> str | Any:
    print(f"apk:{app} >>> ", end="")
    return run_adb("uninstall", app)


def install_app(app) -> str | Any:
    return run_adb("install", app)


def clear_app_data(app) -> str | Any:
    print(f"Clearing appdata... {app}")
    return run_adb("shell", "pm", "clear", app)


def grant_permissions(app, permission) -> str | Any:
    return run_adb("shell", "pm", "grant", app, permission)
