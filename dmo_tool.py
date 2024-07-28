from colorama import Fore, Style
import os
import time
import ipinfo
import socket
import pyperclip 
import sys

RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
CYAN = Fore.CYAN
BLACK = Fore.BLACK
WHITE = Fore.WHITE

def cls():
    os.system('clear')

def intro():
    cls()
    print(RED + """
┳┓┏┳  ┳┳┓┏┓┏┳  ┏┓┳┓┳┏┓┳┳┓┏┓┓
┃┃ ┃  ┃┃┃┃┃ ┃  ┃┃┣┫┃┃┓┃┃┃┣┫┃ 
┻┛┗┛  ┛ ┗┣┛┗┛  ┗┛┛┗┻┗┛┻┛┗┛┗┗┛
_____________________________
██████╗ ███╗   ███╗ ██████╗ 
██╔══██╗████╗ ████║██╔═══██╗
██║  ██║██╔████╔██║██║   ██║
██║  ██║██║╚██╔╝██║██║   ██║
██████╔╝██║ ╚═╝ ██║╚██████╔╝
╚═════╝ ╚═╝     ╚═╝ ╚═════╝ 
_____________________________
Welcome to DMO!
""")
    time.sleep(2)
    cls()

def menu():
    cls()
    print(RED + """
██████╗ ███╗   ███╗ ██████╗ 
██╔══██╗████╗ ████║██╔═══██╗
██║  ██║██╔████╔██║██║   ██║
██║  ██║██║╚██╔╝██║██║   ██║
██████╔╝██║ ╚═╝ ██║╚██████╔╝
╚═════╝ ╚═╝     ╚═╝ ╚═════╝ 
═════════════════════════════
[1] IP Address Lookup
[2] DMO Discord
[3] Check for updates on DMO
[4] Find Your Device's IP
[5] Coming Soon
═════════════════════════════
i love u all :3
[6] To Close DMO
""")

def update_script():
    print(GREEN + "Checking for updates...")
    os.system('git fetch origin main')  

    local_commit = os.popen('git rev-parse HEAD').read().strip()
    remote_commit = os.popen('git rev-parse origin/main').read().strip()

    if local_commit == remote_commit:
        print(RED + "There isn't any newer updates. Please wait until the next update.")
    else:
        os.system('git pull origin main')
        print(GREEN + "Update complete. Restarting script...")
        time.sleep(2)
        cls()
        os.execv(sys.executable, ['python'] + sys.argv)

def iplookup():
    access_token = 'cb657df67f619c'
    handler = ipinfo.getHandler(access_token)

    while True:
        choice = input(">> ")

        if choice == "1":
            ip_address = input("IP >> ")
            details = handler.getDetails(ip_address)
            ip_info = (
                f"IP: {details.ip}\n"
                f"City: {details.city}\n"
                f"Region: {details.region}\n"
                f"Country: {details.country}\n"
                f"Organization: {details.org}\n"
                f"Latitude: {details.latitude}\n"
                f"Longitude: {details.longitude}"
            )
            print(ip_info)
             copy_to_clipboard(ip_info)
            print("Copied to clipboard")
            time.sleep(10)
            cls()
            menu()

        elif choice == "2":
            os.system('termux-open-url https://discord.gg/Q6tK3bAe')
            cls()
            menu()

        elif choice == "3":
            update_script()

        elif choice == "4":
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("Your Device IP Address is:", IPAddr)
            time.sleep(5)
            cls()
            menu()

        elif choice == "5":
            os.system('termux-open-url ""')
            cls()
            menu()

        elif choice == "6":
            cls()
            print("bye love u :3")
            time.sleep(1)
            break

cls()
intro()
menu()
iplookup()
