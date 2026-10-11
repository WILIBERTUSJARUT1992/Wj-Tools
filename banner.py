#!/usr/bin/env python3
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    C = Fore.CYAN
    G = Fore.GREEN
    R = Style.RESET_ALL
except ImportError:
    C = G = R = ""

def show_banner():
    print(C + r"""
 __        ___ _____           _
 \ \      / (_) ____|__   ___ | |___
  \ \ /\ / /| |  _| \ \ / / | |/ __|
   \ V  V / | | |___ \ V /| | | (__ 
    \_/\_/  |_|_____| \_/ |_|_|\___|
""" + R)
    print(G + "             WJ-TOOLS | TERMUX TOOLKIT" + R)
    print("       Utilitas terminal lokal yang sederhana\n")

if __name__ == "__main__":
    show_banner()
