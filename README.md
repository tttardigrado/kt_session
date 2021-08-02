# KT
A kitty session launcher/maker made in python

```sh
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
```
## Config
* The config file is stored at `~/.config/kt/kt_conf.py`
* You can edit it to change 6 things:
    * Create a function to be run at the begining of creation of a new session config
    * Create a function to be run after the creation of a new session config
    * Change the default path to the sessions folder
    * Change the colors for prompts and errors (ANSI)
    * Change the default editor
    * Change the default file manager

## Flags and Commands
* **-h** or **--help** -> shows this message
* **-n** or **--new** -> create a new session file
* **-e** or **--edit** -> edit the config file
* **-e** or **--edit** + **name_of_a_session** -> edit the specified session file
* **-o sessions** or **--open sessions** -> open the sessions folder
* **-o config** or **--open config** -> open the config folder
* **name_of_a_session** -> the specified session will be launched

## Tech stack
**Python**, **kitty** and **markdown**

## Install
Start by cloning the repository
```sh
git clone https://github.com/Force4760/kt_session.git
```

Change to the cloned directory
```sh
cd kt_sessions
```

Install kt
```sh
sh install.sh
# -- or --
pip install -e .
```

*Congratulations!* Now you can run kt_sessions by using the **kt** command and providing the desired arguments or flags


## Default config
```py
# function to be run before a new session is created
# all list elements return will be added
# as lines to the beggining of the session file
def before() -> list:
    return[]

# function to be run after a new session is created
# all list elements return will be added
# as lines to the end of the session file
def after() -> list:
    return[]

# path to the folder where sessions should be stored
path = "~/.config/kitty"

# ANSI color in which any error should be displayed
# it will be used ad \33[color_provided
error_color = "31m"

# ANSI color in which any prompts should be displayed
# it will be used ad \33[color_provided
prompt_color = "32m"

# Editor for the -e flag
editor = "vim"

# File manager for the -o flag
file_manager = "xdg-open"
```
