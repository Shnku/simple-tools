import os
import subprocess
from subprocess import CompletedProcess
import tempfile
from typing import Any
import requests


def run_command(*args: str) -> str | Any:
    command: list[str] = list[str](args)
    result: CompletedProcess = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error executing: " + result.stderr)
        return result.returncode
    return result.stdout.strip()


def run_adb(*args: str) -> str | Any:
    return run_command("adb", *args)


def run_fastboot(*args: str) -> str | Any:
    return run_command("fastboot", *args)


def github_release_download(url_data) -> str:
    response = requests.get(url=url_data)
    response_data = response.json()
    download_path = os.path.join(
        tempfile.gettempdir(), response_data["assets"][0]["name"]
    )
    apk_response = requests.get(
        response_data["assets"][0]["browser_download_url"],
        headers={"Accept": "application/octet-stream", "User-Agent": "Mozilla/5.0"},
        stream=True,
    )
    apk_response.raise_for_status()
    with open(download_path, "wb") as file:
        for chunk in apk_response.iter_content(chunk_size=1024 * 1024):
            print("downloading...")
            file.write(chunk)
    return download_path


def main():
    # Example Usage
    adb_output = run_adb("devices")  # Example adb command
    print(adb_output)

    fastboot_output = run_fastboot("devices")  # Example fastboot command
    print(fastboot_output)


if __name__ == "__main__":
    main()
