import os


def check_config() -> bool:
    '''
    Check if the config file exists.
    If it does returns True
    '''
    path = "~/.config/kt/kt_conf.py"
    path = os.path.expanduser(path)
    return os.path.exists(path)
