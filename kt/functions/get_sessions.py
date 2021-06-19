import os


def get_sessions(path: str) -> list:
    '''
    Get all existing sessions

    Parameters:
        path (str): path to the sessions folder

    Returns:
        (list): list containing the name of the files in the folder
    '''

    # treat path
    path = os.path.expanduser(path)
    # try to get the files
    # on error create the directory
    try:
        files = os.listdir(path)
    except:
        os.makedirs(path)
        files = os.listdir(path)
    return files
