import os


def make_file(path: str, name: str, commands: list, before: list, after: list) -> None:
    '''
    Function to create the session file

    Parameters:
        path (str): path to the kitty sessions folder
        name (str): name of the new session
        commands (list): list of commands to be written to the file
        before (list): list of commands to be written to the file before the ones provided by the user
        after (list): list of commands to be written to the file after the ones provided by the user

    '''

    # prepare the path to the session file
    path = os.path.expanduser(path)
    # path/to/sessions/folder/name.conf
    path = os.path.join(path, f"{name}.conf")

    # open and write to the file
    with open(f"{path}", "w") as f:
        # write before
        for line in before:
            f.write(line + "\n")
        # write user commands
        for line in commands:
            f.write(line + "\n")
        # write after
        for line in after:
            f.write(line + "\n")
