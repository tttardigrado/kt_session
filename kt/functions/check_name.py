def check_name(name: str, files: list) -> bool:
    '''
    Check if the name provided by the user is possible
    Parameters:
        name (str): name provided by the user
        files (list): list of files in the sessions directory
    Returns:
        (bool): if the name is/is not valid
    '''
    # process name
    name = name.strip() + ".conf"

    # loop through the files
    # to see if the name is already in use
    for i in files:
        if i == name:
            return False
    return True
