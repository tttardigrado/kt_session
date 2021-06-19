from ..functions import get_sessions, check_name
from .colors import input_color, print_color


def get_name(path: str, colors: list) -> str:
    '''
    Function to get a name for the session

    Parameters:
        path (str): path to the kitty sessions folder
        colors (list): [prompt, error], colors to be used

    Returns:
        (str): possible name for the session
    '''

    # get a list of currently existing session
    sessions = get_sessions(path)

    # ask the user for a name until that name is available
    while True:
        # ask for name
        name = input_color("New Session Name: ", colors[0])
        # check if the provided name is available
        is_possible = check_name(name, sessions)
        if is_possible:
            break
        else:
            # print message saying that the name is unavailable
            print_color("Sorry. That Session already exists.", colors[1])
            continue
    return name
