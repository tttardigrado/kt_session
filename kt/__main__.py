from .flags import new_flag, help_flag, normal_flag, edit_flag, open_flag, edit_config_flag
from .functions import check_config, load_config
import sys


def main():
    '''
    Main function of the program
    '''
    try:
        arg = sys.argv[1:]
    # if there is no argument/flag
    except IndexError:
        arg = ""

    # check and load the config
    check = check_config()
    config = load_config(check)

    # if the argument/flag was provided
    if arg:
        # new session
        if arg[0] == "-n" or arg[0] == "--new":
            new_flag(config)
        # help
        elif arg[0] == "-h" or arg[0] == "--help":
            help_flag(config)
        # edit
        elif arg[0] == "-e" or arg[0] == "--edit":
            # if an argument is provided besides the flag
            if len(arg) >= 2:
                edit_flag(arg[1], config)
            else:
                edit_config_flag(config)
        # open
        elif arg[0] == "-o" or arg[0] == "--open":
            # if an argument is provided besides the flag
            if len(arg) >= 2:
                open_flag(arg[1], config)
            else:
                open_flag("sessions", config)
        # run a session
        # arg would be the session name
        else:
            normal_flag(arg[0], config)
    # on no argument run help
    else:
        help_flag(config)


if __name__ == "__main__":
    main()
