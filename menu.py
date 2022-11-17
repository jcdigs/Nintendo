import math
import os
import fontstyle
import time

from colorama import init
from termcolor import colored

Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
black = "\033[0;90m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
cyan_back="\033[0;46m"
pink_back="\033[0;45m"
white_back="\033[0;47m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
green_back="\033[0;42m"
red_back="\033[0;41m"
grey_back="\033[0;40m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
reset = "\033[0m"

init()

playing = True

while(playing):

    print(fontstyle.apply('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))
    print(yellow + '::' + cyan + '                                                      __  ___                  ' + yellow + '                                                   ::')
    print(yellow + '::' + cyan + '                                                     /  \/  /___ ____  __  __  ' + yellow + '                                                   ::')
    print(yellow + '::' + cyan + '                                                    /  \/  // _ \ __ \/ / / /  ' + yellow + '                                                   ::')
    print(yellow + '::' + cyan + '                                                   /  / / //   _/ // / /_/ /   ' + yellow + '                                                   ::')
    print(yellow + '::' + cyan + '                                                  /__/ /_/ \___/_//_/\__,_/    ' + yellow + '                                                   ::')
    print(fontstyle.apply('::                                                                                                                                  ::', 'yellow'))
    print(fontstyle.apply('::                                                                                                                                  ::', 'yellow'))
    print(fontstyle.apply('::                                                                                                                                  ::', 'yellow'))
    print(yellow + ':: ' + cyan + '                                                        >  Play              ' + yellow + '                                                    ::')
    print(yellow + ':: ' + cyan + '                                                        >  About             ' + yellow + '                                                    ::')
    print(yellow + ':: ' + cyan + '                                                        >  Settings          ' + yellow + '                                                    ::')
    print(yellow + ':: ' + cyan + '                                                        >  Account           ' + yellow + '                                                    ::')
    print(fontstyle.apply('::                                                                                                                                  ::', 'yellow'))
    print(fontstyle.apply('::                                                                                                                                  ::', 'yellow'))
    print(fontstyle.apply('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))
    print(fontstyle.apply('::::::::::::::Type 1: Play:::::::::::::::Type 2: About::::::::::::::::Type 3: Settings::::::::::::::::::Type 4: Account:::::::::::::::', 'yellow'))
    print(fontstyle.apply('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))

    userInput = input(fontstyle.apply("Choose from 1-4: ", "bold/red"))

    if userInput == "S":
        playing = os.system('python menu.py')
    elif userInput != playing:
        break