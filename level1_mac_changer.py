#!/usr/bin/env python
'''
Level 1 :- basic comman.txt in python

> now this a auto mac changer program but you need to enter mac address manually

how to run program
>> python level1_mac_changer.py
'''
import subprocess       # python defult packets

# useing call function for command
subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
subprocess.call("ifconfig wlan0", shell=True)
