import os
from typing import Any, Callable, Dict
from functionality.command_runner import run_adb


def list_devices() -> str | Any:
    return run_adb("devices")


def adb_help() -> str | Any:
    return run_adb("--help")


def adb_version() -> str | Any:
    return run_adb("--version")


ADB_COMMANDS: Dict[str, Callable[..., Any]] = {
    # Device management
    "List devices": lambda: run_adb("devices"),
    "ADB help": lambda: run_adb("--help"),
    "ADB version": lambda: run_adb("--version"),
    # Reboot options
    "Reboot device": lambda: run_adb("reboot"),
    "Boot fastboot": lambda: run_adb("reboot", "bootloader"),
    "Boot recovery": lambda: run_adb("reboot", "recovery"),
    # App management
    "List apps": lambda: run_adb("shell", "pm", "list", "packages"),
    "Remove app": lambda app: run_adb("uninstall", app),
    "Install app": lambda app: run_adb("install", app),
    "Clear app data": lambda app: run_adb("shell", "pm", "clear", app),
    "Grant permission": lambda app, permission: run_adb(
        "shell", "pm", "grant", app, permission
    ),
    # File operations
    "Push file": lambda file: run_adb("push", file, "/sdcard/Download/"),
    "Pull file": lambda location,
    downloads_dir=os.path.expanduser("~/Downloads"): run_adb(
        "pull", location, downloads_dir
    ),
    # Debugging & logs
    "View logs": lambda: run_adb("logcat"),
    "Clear logs": lambda: run_adb("logcat", "-c"),
    # "Screenshot": lambda: run_adb("shell", "screencap", "-p", "/sdcard/screen.png"),
    # "Screenrecord": lambda duration=10: run_adb(
    #     "shell", "screenrecord", f"--time-limit={duration}", "/sdcard/screen.mp4"
    # ),
    # # Shell & system
    # "Open shell": lambda: run_adb("shell"),
    # "Kill server": lambda: run_adb("kill-server"),
    # "Start server": lambda: run_adb("start-server"),
    # "Remount RW": lambda: run_adb("remount"),
    # "Get state": lambda: run_adb("get-state"),
    # # App actions
    # "Launch app": lambda pkg: run_adb("shell", "am", "start", f"-n {pkg}"),
    # "Force stop app": lambda pkg: run_adb("shell", "am", "force-stop", pkg),
    # "Kill app": lambda pkg: run_adb("shell", "am", "kill", pkg),
    # "List activities": lambda pkg: run_adb(
    #     "shell", "cmd", "package", "list", "activities", pkg
    # ),
    # # Backups
    # "Backup app": lambda pkg: run_adb("backup", "-apk", pkg),
    # "Restore backup": lambda file: run_adb("restore", file),
    # # Input & simulation
    # "Simulate tap": lambda x, y: run_adb("shell", "input", "tap", x, y),
    # "Simulate key": lambda keycode: run_adb("shell", "input", "keyevent", keycode),
    # # Network & wireless
    # "TCP/IP mode": lambda port=5555: run_adb("tcpip", port),
    # "Connect wireless": lambda ip_port: run_adb("connect", ip_port),
    # "Disconnect wireless": lambda: run_adb("disconnect"),
}
