from .colors import input_color, print_color


def read_commands(colors: list, allLines: list = []) -> list:
    '''
    Function to read and store the commands provided by the user

    Parameters:
        colors (list): [promt, error], list of colors to be used
        allLines (list): list of pre-loaded commands
    '''
    # ask for the first command
    allLines.append(input_color("Command: ", colors[0]))
    # ask for multiple commands
    while True:
        # check if the user wants to add more commands
        new = input_color("New Command? (Y/N): ", colors[0])
        if new == "N" or new == "n":
            break
        # ask for a new command
        allLines.append(input_color("Command: ", colors[0]))
        continue
    return allLines
