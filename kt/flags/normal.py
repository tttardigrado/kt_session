import os
from ..functions import load_config, check_config
from .help import help_flag
from ..user import print_color


def normal_flag(name: str, config: dict) -> None:
    '''Function used when no flag is provided

    Parameters:
        name (str): name of the session
        config (dict): dictionary containing the config
    '''

    # treat path
    path = os.path.expanduser(config["path"])
    path = os.path.join(path, f"{name}.conf")

    if os.path.exists(path):
        # run kitty session
        command = f"kitty --detach --session {path}"
        os.system(command)
    else:
        print_color("Sorry! That session does not exist!", config["colors"][1])
        help_flag(config)
