from ..functions import check_config, load_config, make_file
from ..user import get_name, read_commands


def new_flag(config: dict) -> None:
    '''
    Function to handle the -n or --new flag

    Parameters:
        config (dict): dictionary containing the config
    '''

    # list of commands to "pre type" to the session file
    before_list = config["before"]()
    # gte the name for the session
    name = get_name(config["path"], config["colors"])
    # read all the user-provided commands
    commands = read_commands(config["colors"])
    # list of commands to "post type" to the session file
    after_list = config["after"]()

    # create the session file
    make_file(config["path"], name, commands, before_list, after_list)
