#######################################################
# Name           : Brute Facebook (BF)                #
# File           : logo.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############


import sys, os

#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel
biru_m = '[bold cyan]'
hapus  = '[/]'


class Logo:

    def __init__(self):
        if "linux" in sys.platform.lower():
            try:os.system("clear")
            except:pass
        elif "win" in sys.platform.lower():
            try:os.system("cls")
            except:pass
        else:
            try:os.system("clear")
            except:pass

    def log(self):
        prints(Panel(f"""{biru_m} __  __        __  ______  ____{hapus}
{biru_m} \ \/ / ____  /  |/  / _ )/ __/ ® {hapus}|| Created By YayanXD
{biru_m}  \  / /___/ / /|_/ / _  / _/     {hapus}|| Github.com/Yayan-XD
{biru_m}  /_/       /_/  /_/____/_/ v3.0  {hapus}|| Facebook.com/KM39453"""))
