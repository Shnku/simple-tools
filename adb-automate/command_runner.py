import subprocess
from subprocess import CompletedProcess
from typing import Any


def run_command(*args: str) -> str | Any:
    command: list[str] = list(args)
    result: CompletedProcess = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error executing: " + result.stderr)
        return result.returncode
    return result.stdout.strip()


def run_adb(*args: str) -> str | Any:
    return run_command("adb", *args)


def run_fastboot(*args: str) -> str | Any:
    return run_command("fastboot", *args)


# Example Usage
adb_output = run_adb("devices")  # Example adb command
print(adb_output)

fastboot_output = run_fastboot("devices")  # Example fastboot command
print(fastboot_output)
