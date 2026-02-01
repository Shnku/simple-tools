# For windows systems, this script checks for and installs necessary ADB drivers using winget.

from functionality.command_runner import run_command

# Define packages to check and install
PACKAGES = {
    "Android SDK Platform-Tools": "Google.PlatformTools",
    "Universal Adb Driver": "ClockworkMod.UniversalADBDriver",
}


def check_installed(package):
    try:
        output = run_command(f"winget list | findstr {package}", shell=True)
        return package in output
    except Exception:
        return False


def install_package(package):
    try:
        print(f"Installing {package}...")
        out = run_command(
            "winget",
            "install",
            "--exact",
            "--accept-package-agreements",
            "--accept-source-agreements",
            package,
        )
        print(f"Successfully installed {package}")
        return out
    except Exception as e:
        print(f"Failed to install {package}: {str(e)}")
        return e


def main():
    # Check and install PACKAGES
    for name, package in PACKAGES.items():
        if check_installed(package) is True:
            print(f"{name.capitalize()} is already installed.")
        else:
            install_package(package)


if __name__ == "__main__":
    main()
