from ..user import print_color
from .help import help_flag
import os


def edit_flag(name: str, config: dict) -> None:

    # treat path
    path = os.path.expanduser(config["path"])
    path = os.path.join(path, f"{name}.conf")

    if os.path.exists(path):
        # run session
        command = f"{config['editor']} {path}"
        os.system(command)
    else:
        # throw an error and run help
        print_color("Sorry! That file does not exist!", config["colors"][1])
        help_flag(config)


def edit_config_flag(config: dict) -> None:

    # treat path
    path = os.path.expanduser("~/.config/kt/kt_conf.py")

    if os.path.exists(path):
        # run session
        command = f"{config['editor']} {path}"
        os.system(command)
    else:
        # throw an error and run help
        print_color("Sorry! That file does not exist!", config["colors"][1])
        help_flag(config)
