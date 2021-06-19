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
