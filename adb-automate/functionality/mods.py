from typing import Any
from command_runner import run_adb


# functions related to mods installations...........


def activate_shizuku() -> str | Any:
    path: str | Any = run_adb(
        "shell", "pm", "path", "--user", "0", "moe.shizuku.privileged.api"
    )
    print(path.split(sep=":"))
    dir_name: str | Any = run_adb("shell", "dirname", path[1])
    lib_path: str | Any = dir_name.join("/lib/*/libshizuku.so")
    return run_adb("shell", lib_path)
