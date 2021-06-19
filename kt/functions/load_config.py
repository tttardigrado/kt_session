import sys
import os


def base_fun_before() -> list:
    return []


def base_fun_after() -> list:
    return []


def load_config(config_exists: bool) -> dict:
    '''
    Function to load the config

     Returns:
        (dict): dictionary containing before, after, path, colors, editor and file_manager.
    '''
    if config_exists:
        config = config_exists_function()
    else:
        config = config_not_exists_function()
    config_dict = {
        "before": config[0],
        "after": config[1],
        "path": config[2],
        "colors": config[3],
        "editor": config[4],
        "file_manager": config[5]
    }
    return config_dict


def config_exists_function() -> tuple:
    '''
    Function used when there is a config file

    Returns:
        (tuple): ((function) before, (function) after, (str) path to sessions folder, (list) colors)
    '''

    # import the config file
    path_to_config = os.path.expanduser("~/.config/kt")
    sys.path.insert(0, path_to_config)
    import kt_conf

    # before function
    try:
        fun_b = kt_conf.before
    except:
        fun_b = base_fun_before

    # after function
    try:
        fun_a = kt_conf.after
    except:
        fun_a = base_fun_after

    # path to sessions folder
    try:
        path = kt_conf.path
    except:
        path = "~/.config/kitty"

    # prompt color
    try:
        prompt_color = kt_conf.prompt_color
    except:
        prompt_color = "32m"

    # error color
    try:
        error_color = kt_conf.error_color
    except:
        error_color = "31m"

    # text editor
    try:
        editor = kt_conf.editor
    except:
        editor = "vim"

    # text editor
    try:
        file_manager = kt_conf.file_manager
    except:
        file_manager = "xdg-open"

    return fun_b, fun_a, path, [prompt_color, error_color], editor, file_manager


def config_not_exists_function() -> tuple:
    '''
    Function used when there is no config file in the system

    Returns:
        (tuple): ((function) before, (function) after, (str) path to sessions folder, (list) colors)
    '''

    # default configuration file
    default_config = """
def before() -> list:
    return[]


def after() -> list:
    return[]


path = "~/.config/kitty"

error_color = "31m"

prompt_color = "32m"

editor = "vim"

file_manager = "xdg-open"

    """

    # create the config dir and file
    path = "~/.config/kt/kt_conf.py"
    path = os.path.expanduser(path)
    os.makedirs(path)

    # write to the config file
    with open(path, "w") as f:
        f.write(default_config)

    # return the defaults
    fun_b = base_fun_before

    fun_a = base_fun_after

    path = "~/.config/kitty"

    colors = ["32m", "31m"]

    editor = "vim"

    file_manager = "xdg-open"

    return fun_b, fun_a, path, colors, editor, file_manager
