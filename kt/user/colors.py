def print_color(msg: str, color: str) -> None:
    '''
    Function to print colored output

    Parameters:
        msg (str): the message to be printed
        color (str): ANSI color code (ex: 31m or \33[31m would be red)
    '''
    # prepare color
    if not color.startswith("\33["):
        color = "\33[" + color
    print(color + msg + "\033[0m")


def input_color(msg: str, color: str) -> str:
    '''
    Function to get input with a colored message

    Parameters:
        msg (str): the message to be printed
        color (str): ANSI color code (ex: 31m would be red)

    Returns:
        (str): the redult from a regular input function
    '''
    # prepare color
    if not color.startswith("\33["):
        color = "\33[" + color

    return input(color + msg + "\033[0m")
