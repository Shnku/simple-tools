from command_runner import run_adb


def activate_shizuku():
    path = run_adb("shell", "pm", "path", "--user", "0", "moe.shizuku.privileged.api")
    print(path.split(":"))
    dir_name = run_adb("shell", "dirname", path[1])
    lib_path = dir_name.join("/lib/*/libshizuku.so")
    run_adb("shell", lib_path)


