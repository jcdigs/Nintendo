import math
import os
import fontstyle
import time

from tqdm import tqdm , trange
from colorama import init
from termcolor import colored

init()

# pbar = tqdm(total = 100)
# for i in range(10):
#   time.sleep(0.5)
#   pbar.update(10)
# pbar.close()

playing = True

while(playing):

  print(fontstyle.apply('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))
  print(fontstyle.apply('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))

  print(fontstyle.apply("Welcome to...","yellow"))
  print(fontstyle.apply("""
                  
      ███████╗██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗    ███╗   ██╗██╗███╗   ██╗████████╗███████╗███╗   ██╗██████╗  ██████╗     
      ██╔════╝██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝    ████╗  ██║██║████╗  ██║╚══██╔══╝██╔════╝████╗  ██║██╔══██╗██╔═══██╗
      █████╗  ██║   ██║   ██║   ██║   ██║██████╔╝█████╗      ██╔██╗ ██║██║██╔██╗ ██║   ██║   █████╗  ██╔██╗ ██║██║  ██║██║   ██║
      ██╔══╝  ██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝      ██║╚██╗██║██║██║╚██╗██║   ██║   ██╔══╝  ██║╚██╗██║██║  ██║██║   ██║
      ██║     ╚██████╔╝   ██║   ╚██████╔╝██║  ██║███████╗    ██║ ╚████║██║██║ ╚████║   ██║   ███████╗██║ ╚████║██████╔╝╚██████╔╝
      ╚═╝      ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝     

                                                                  o
                                                          o       /
                                                          \     /
                                                            \   /
                                                            \ /
                                                        ______________
                                                      |.------------.|
                                                      ||            ||
                                                      ||            ||
                                                      ||            ||
                                                      ||            ||
                                                      ||____________||_
                                                      |OO ....... OO | `-.
                                                      '------_.-._---' _.'  
                                                        _____||   ||___/_
                                                      /  _.-|| N ||-._  \      .-._
                                                      / -'_.---------._'- \    ,'___i--i___
                                                    /_.-'_  NINTENDO _'-._\  ' /_+  o :::__\'
                                                    |`-i /m\/m\|\|/=,/m\i-'|  | || \ O / ||
                                                akg |  |_\_/\_/___\_/'./|  |  | \/  \ /  \/
                                                    `-'              '-.`-'  ,      V
                                                                        `---'
      """, "yellow"))

  print(fontstyle.apply("                                                                                                                  Designed by: The J's","yellow"))
  print(fontstyle.apply('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))
  print(fontstyle.apply('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))
  print(fontstyle.apply("                                                                                                                    Created: 2022-2023", "bold/italic/green"))
  print(fontstyle.apply('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))

  userInput = input(fontstyle.apply("Type S to Start: ", "bold/red"))

  if userInput == "S":
     playing = os.system('python menu.py')
  elif userInput != playing:
    break
