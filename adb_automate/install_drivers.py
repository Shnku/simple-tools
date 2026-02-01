import subprocess

from functionality.command_runner import run_command

# Define packages to check and install
PACKAGES = {
    "Android SDK Platform-Tools": "Google.Platformtools",
    "Universal Adb Drivers": "ClockworkMod.UniversalADBDrivers",
}


def check_installed(package):
    try:
        output = run_command("winget", "list", "|", "findstr", package)
        return package in output
    except subprocess.CalledProcessError:
        return False


def install_package(package):
    print(f"Installing {package}...")
    try:
        out = run_command("winget", "install", "--exace", "--silent", package)
        return out
    except Exception as e:
        return e


def main():
    # Check and install PACKAGES
    for name, package in PACKAGES.items():
        if check_installed(package):
            print(f"{name.capitalize()} is already installed.")
        else:
            install_package(package)


if __name__ == "__main__":
    main()
