from colorama import Fore, Style 
import os
import time
import ipinfo
import socket

RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
CYAN = Fore.CYAN
BLACK = Fore.BLACK
WHITE = Fore.WHITE

print(RED + " DMO MultiTool Booting... ")
time.sleep(2)

def cls():
    os.system('clear')

def intro():
    print(RED + """
┳┓┏┳  ┳┳┓┏┓┏┳  ┏┓┳┓┳┏┓┳┳┓┏┓┓
┃┃ ┃  ┃┃┃┃┃ ┃  ┃┃┣┫┃┃┓┃┃┃┣┫┃ ___________________________
┻┛┗┛  ┛ ┗┣┛┗┛  ┗┛┛┗┻┗┛┻┛┗┛┗┗┛                 
  ██████╗ ███╗   ███╗ ██████╗          
  ██╔══██╗████╗ ████║██╔═══██╗       
[ ██║  ██║██╔████╔██║██║   ██║ - Multitool ]
  ██║  ██║██║╚██╔╝██║██║   ██║
  ██████╔╝██║ ╚═╝ ██║╚██████╔╝
  ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ 
                           ____________________________
Welcome to DMO Multitool!

""")
intro()
time.sleep(2)
cls()

def menu():
    print(RED + """

                                                        
                                                     ██████╗ ███╗   ███╗ ██████╗ 
                                                     ██╔══██╗████╗ ████║██╔═══██╗
                                                     ██║  ██║██╔████╔██║██║   ██║
                                                     ██║  ██║██║╚██╔╝██║██║   ██║
                                                     ██████╔╝██║ ╚═╝ ██║╚██████╔╝
                                                    ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ 

                                                            use [6.] to exit.


                   ══════════════════════════════════════════════════════════════════════════════════
                                                                [ USER ] 
                                            
                                            [1] IP Address Lookup               [4] Find Your Device's IP

                                            [2] DMO Discord                     [5] soon

                                            [3] Check for updates on DMO

                    ══════════════════════════════════════════════════════════════════════════════════
                                                         i love u all :3
                                                        use [6.] to exit.
""")

def iplookup():
    access_token = 'cb657df67f619c'
    handler = ipinfo.getHandler(access_token)

    while True:
        choice = input("                                >> ")

        if choice == "1":
            ip_address = input(f"                             IP >> ")
            details = handler.getDetails(ip_address)
            print("                                 IP:", details.ip)
            print("                                 City:", details.city)
            print("                                 Region:", details.region)
            print("                                 Country:", details.country)
            print("                                 Organization:", details.org)
            print("                                 Latitude:", details.latitude)
            print("                                 Longitude:", details.longitude)
            time.sleep(5)
            cls()
            menu()

        elif choice == "2":
            os.system('termux-open-url https://discord.gg/Q6tK3bAe')
            cls()
            menu()

        elif choice == "3":
            os.system('termux-open-url https://github.com/umsoidonthavethegithubsetupyetsoilldoitnextupd')

        elif choice == "4":
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("Your Device IP Address is:", IPAddr)

        elif choice == "5":
            os.system('termux-open-url ""')

        elif choice == "6":
            print("                                bye love u :3 ")
            time.sleep(1)
            break

cls()
menu()
iplookup()
