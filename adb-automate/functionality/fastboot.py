from typing import Any, Callable, Dict
from command_runner import run_fastboot


def list_devices() -> str | Any:
    return run_fastboot("devices")


def fastboot_help() -> str | Any:
    return run_fastboot("--help")


def boot_recovery() -> str | Any:
    return run_fastboot("reboot", "recovery")


FASTBOOT_COMMANDS: Dict[str, Callable[..., Any]] = {
    # Device info & status
    "List devices": lambda: run_fastboot("devices"),
    "Show variables": lambda: run_fastboot("getvar", "all"),
    # Boot & reboot
    "Reboot device": lambda: run_fastboot("reboot"),
    "Reboot bootloader": lambda: run_fastboot("reboot-bootloader"),
    "Reboot recovery": lambda: run_fastboot("reboot", "recovery"),
    # Bootloader unlock/lock
    "Unlock bootloader": lambda: run_fastboot("oem", "unlock"),
    "Unlock bootloader (new)": lambda: run_fastboot("flashing", "unlock"),
    "Lock bootloader": lambda: run_fastboot("oem", "lock"),
    "Lock bootloader (new)": lambda: run_fastboot("flashing", "lock"),
    # Flashing
    "Flash partition": lambda partition, img: run_fastboot("flash", partition, img),
    "Flash boot": lambda img: run_fastboot("flash", "boot", img),
    "Flash recovery": lambda img: run_fastboot("flash", "recovery", img),
    "Flash system": lambda img: run_fastboot("flash", "system", img),
    "Boot image (temp)": lambda img: run_fastboot("boot", img),
    # Erase & wipe
    "Erase partition": lambda partition: run_fastboot("erase", partition),
    "Format partition": lambda partition: run_fastboot("format", partition),
    "Wipe userdata/cache": lambda: run_fastboot("-w"),
    # A/B slots (modern devices)
    "Set active slot": lambda slot: run_fastboot("--set-active", slot),
    "Get current slot": lambda: run_fastboot("getvar", "current-slot"),
    # OEM/device-specific
    "Continue boot": lambda: run_fastboot("continue"),
    "Disable verity": lambda: run_fastboot("disable-verity"),
    "Enable verity": lambda: run_fastboot("enable-verity"),
}
