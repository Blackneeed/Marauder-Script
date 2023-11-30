import os
import time
from settings import Settings
from files import *
from screen import *
from attacks import *

settings = Settings
log_file = settings['log_file']

def clear_log():
    fileminus(log_file)

def menu():
    cls()
    print("[1: Add attack]")
    choice = input("Enter the number of your choice: ")
    if not choice.isnumeric():
        print(f"{choice} is not a valid number!")
        time.sleep(3)
        menu()
    elif choice not in ["1"]:
        print(f"{choice} is not a valid option!")
        time.sleep(3)
        menu()
    elif choice == "1":
        add_attack()

def add_attack():
    cls()
    print("Add attack:")
    print("[1: Beacon]\n[2: Deauth]\n[3: Back]")
    attack = input("Enter the number of your choice: ")
    if not attack.isnumeric():
        print(f"{attack} is not a valid number!")
        time.sleep(3)
        add_attack_beacon()
    elif attack not in ["1", "2", "3"]:
        print(f"{attack} is not a valid option!")
        time.sleep(3)
        add_attack()
    elif attack == "1":
        add_attack_beacon()
        add_attack()
    elif attack == "2":
        add_attack_deauth()
        add_attack()
    elif attack == "3":
        menu()

clear_log()
cls()
logo()
time.sleep(3)
lnskip()
menu()