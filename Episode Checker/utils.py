import os
import requests

from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_soup(page_url):
    """ Returns BeautifulSoup object of the url provided """
    try:
        req = requests.get(page_url)
    except Exception:
        print('Failed to establish a connection with the website')
        return
    if req.status_code == 404:
        print('Page not found')
        return

    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def zero_prefix(num):
    """ Adds '0' as a prefix to numbers less than 10 """
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)


def is_internet_connected():
    """ Checks if the computer is connected to the internet """
    try:
        urlopen('http://216.58.192.142', timeout=1)  # '216.58.192.142' is one of the IPs of www.google.com
        return True
    except Exception:
        return False


def path_check(path, folder):
    """ Check if the folder for the respective series exists, otherwise create a new folder """
    if folder not in os.listdir(path):
        os.mkdir(path + folder)


def display(series, season, episode, title):
    print(series, 'Season', season + ': Episode', episode, title)


def download_file(file_name, url):
    """ Use this function if you want to download the episode from the terminal """
    req = requests.get(url)

    if req.status_code == 404 or '404' in req.url:
        print('No such file found')
        return

    if file_name in str(req.content):
        print('File found')
        filename = url.split('/')[-1]
        print('Downloading...')
        with open(filename, 'wb') as fobj:
            fobj.write(req.content)
        print('Download complete')
    else:
        print('error')
