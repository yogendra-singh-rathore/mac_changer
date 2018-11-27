#!/usr/bin/env python

'''
Mac_Changer
    Simple Algorith

Goal ---> Check if MAC Address was change

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Step:-
    1. Execute and read ifconfig
    2. Read the MAC Address from output
    3. Check if MAC in ifconfig is what the user requested
    4. Print appropriate message.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
we are using Regex: because we only focus on MAC Address so we filter out our MAC address
    >>> Regex   [Website:-  www.pythex.org]
        *Search for specific patterns within a string
        *Uses rules to match pattern
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
How to run this program
eg:-
1 > python final_Mac_Changer.py -i wlan0 -m 00:11:22:33:44:99
2 > python final_Mac_Changer.py --interface wlan0 --mac 00:11:22:33:44:99
3 > python final_Mac_Changer.py -i eth0 -m 00:11:22:33:44:99
4 > python final_Mac_Changer.py -i lo -m 00:11:22:33:44:99
'''

import subprocess
import optparse
import re

def get_value():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC Addess")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Addess")
    (options, value) = parser.parse_args()
    if not options.interface:   # handel error if user not enter input
        parser.error("[-] Please specify an interface, using --helo or -h for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify an New MAC, using --helo or -h for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac )
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_new_mac(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface])
    mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:", ifconfig_output)

    if mac_search:
        return mac_search.group(0)
    else:
        print("[-] Could not read MAC Address.")


options = get_value()

current_mac = get_new_mac(options.interface)
print("current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac) #call our function and give the value

current_mac = get_new_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")
