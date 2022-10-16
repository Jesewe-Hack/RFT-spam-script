import keyboard as k
import webbrowser
import time
import ctypes
from colorama import init, Fore
import os
init(autoreset=True)

ctypes.windll.kernel32.SetConsoleTitleW('RFT SPAM 2 | By f0rk1l | Edited by Jesewe')

def spam():
    while True:
        try:
            print(Fore.GREEN + 'Launching a spam attack in 5 seconds...')
            time.sleep(5)
            with open(r'messages.txt', 'r',encoding='latin-1') as file: # считывание файла
                for t in file:
                    k.write(t, 0.02)
                    k.send("enter")
                    time.sleep(1)
                    print(Fore.GREEN + f"\n[+] Message sent: {t}")
        except Exception as e:
            print(Fore.RED + f'\n[-] Unsent message: {t}')

banner="""
                ________________________________   ___________________  _____      _____   
                \______   \_   _____/\__    ___/  /   _____/\______   \/  _  \    /     \  
                 |       _/|    __)    |    |     \_____  \  |     ___/  /_\  \  /  \ /  \ 
                 |    |   \|     \     |    |     /        \ |    |  /    |    \/    Y    \  
                 |____|_  /\___  /     |____|    /_______  / |____|  \____|__  /\____|__  /  
                        \/     \/                        \/                  \/         \/    
                                       Made by f0rk1l, Jesewe
"""

os.system('cls')
print(Fore.RED + banner)
print(Fore.GREEN + "\nWelcome to RFT SPAM 2, select an action:\n")
print(Fore.RED + "[0] Exit\n[1] Start Spam Script\n[2] Information")
try:
    chooser=int(input(Fore.YELLOW + '\nYour Action : '))
    if chooser == 0:
        print(Fore.RED + 'Exit...')
        os.abort()
    elif chooser == 1:
        try:
            spam()
        except:
            print(Fore.RED + '\n━━━━━━━━━━Error━━━━━━━━━━━━━━━━━━━━━━')
            input(Fore.RED + '━━━━━━━━━━Press Enter to exit━━━━━━━━━━')
    elif chooser == 2:
        print(Fore.GREEN + "\nThis software is an advanced version of the spam script, I don't think that the interface needs to be explained, it is already intuitive.\nBriefly about the work of the script: after activation, you will have 5 seconds to run the program you want. After launching and hovering the cursor over the input field, the spam script itself will start entering and sending messages from the text prepared in the 'messages.txt' file.\nHow to run the script?: Run the included program and select action №1 (the 'messages.txt' file must be in the same directory as the exe file itself, otherwise the software will give an error)")
        input(Fore.RED + '\n━━━━━━━━━━Press Enter to exit━━━━━━━━━━')
    else:
        print(Fore.RED + '\n━━━━━━━━━━Invalid Value━━━━━━━━━━━━━━')
        input(Fore.RED + '━━━━━━━━━━Press Enter to exit━━━━━━━━')
except Exception as e:
    print(Fore.RED + '\n━━━━━━━━━━Invalid Value━━━━━━━━━━━━━━')
    input(Fore.RED + '━━━━━━━━━━Press Enter to exit━━━━━━━━')