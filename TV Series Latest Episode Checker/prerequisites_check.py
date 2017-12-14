""" This module makes sure that all the prerequisites are met before checking or downloading new episodes.
"""

import os

from urllib.request import urlopen


# Checks if the computer is connected to the internet
def is_internet_connected():
    try:
        urlopen('http://216.58.192.142', timeout=1)     # '216.58.192.142' is one of the IPs of www.google.com
        return True
    except Exception:
        return False


# Check if the folder for the respective series exists, otherwise create a new folder
def path_check(path, folder):
    if folder not in os.listdir(path):
        os.mkdir(path + folder)
