from ..user import print_color
from .help import help_flag
import os


def open_flag(folder: str, config: dict) -> None:
    '''
    Function to open either the config folder or the sessions folder
    Parameters:
        folder (str): either "config" or "sessions"
        config (dict): dictionary containing the config
    '''

    if folder == "config":
        # treat path
        path = os.path.expanduser("~/.config/kt")
    else:
        # treat path
        path = os.path.expanduser(config["path"])

    if os.path.exists(path):
        # run session
        command = f"{config['file_manager']} {path}"
        os.system(command)
    else:
        # throw an error and run help
        print_color("Sorry! That folder does not exist!", config["colors"][1])
        help_flag(config)
