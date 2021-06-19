from ..functions import check_config, load_config
from ..user import print_color


def help_flag(config: dict) -> None:
    '''
    Function to handle the -h or --help flag

    Parameters:
        config (dict): dict with config
    '''

    msg = r"""
    ######################################################
    #  _______   _______   _______    _______   _______  #
    # |  _____| |  ___  | |  ___  |  |  _____| |  _____| #
    # | |___    | |   | | | |___| |  | |       | |_____  #
    # |  ___|   | |   | | |  ___  |  | |       |  _____| #
    # | |       | |___| | | |   \ \  | |_____  | |_____  #
    # |_|       |_______| |_|    \_\ |_______| |_______| #
    #                                                    #
    # Made by Force4760                                  #
    ######################################################
    """
    print_color("## Config:", config["colors"][0])
    print("  -> The config file is stored at '~/.config/kt/kt_conf.py'")
    print("  -> You can edit it to change 6 things:")
    print("    -> Create a function to be run at the begining of creating a new session config")
    print("    -> Create a function to be run after the creating a new session config")
    print("    -> Change the default path to the sessions folder")
    print("    -> Change the colors for prompts and errors (ANSI)")
    print("    -> Change the default editor")
    print("    -> Change the default file manager\n\n")
    print_color("## Flags and Commands:", config["colors"][0])
    print("  -> -h or --help -> shows this message")
    print("  -> -n or --new -> create a new session file")
    print("  -> -e or --edit -> edit the config file")
    print("  -> -e or --edit + name_of_a_session -> edit the specified session file")
    print("  -> -o sessions or --open sessions -> open the sessions folder")
    print("  -> -o config or --open config -> open the config folder")
    print("  -> name_of_a_session -> the specified session will be launched\n")
    print_color(msg, config["colors"][0])
