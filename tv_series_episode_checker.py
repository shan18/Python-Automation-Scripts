#!/usr/bin/env python3

""" This script checks for the new episodes of TV series and anime and gives the download link
    Enter the path name and the url of the website accordingly.
"""

import requests
import os
import sys
from urllib.request import urlopen


""" Checks if the computer is connected to the internet
"""
def is_internet_connected():
    try:
        urlopen('http://216.58.192.142', timeout=1)     # '216.58.192.142' is one of the IPs of www.google.com
        return True
    except Exception as err:
        return False


""" Use this function if you want to download the episode from termminal
"""
def download(file_name, url):
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


def check(tv_anime, series_name, page_url, episode_name):
    req = requests.get(page_url)

    if req.status_code == 404:
        print('Page not found')
        return
    
    if episode_name in str(req.content) and '404' not in str(req.url):
        print(series_name + ':')
        if tv_anime == 'tv':
            print(page_url + episode_name, end='\n\n')
        else:
            page_url_split = page_url.split('/')
            if series_name.startswith('Boruto'):
                page_url_split[-2] = page_url_split[-2][:-1]
            anime_download_link = '/'.join([page_url_split[0] + '/', page_url_split[2],
                                            '-'.join([page_url_split[4], page_url_split[3], episode_name.split()[-1],
                                                      'english-subbed'])])
            print(anime_download_link, end='\n\n')


""" Check if the folder for the respective series exists, otherwise create a new folder
"""
def path_check(path, folder):
    if folder not in os.listdir(path):
        os.mkdir(path + folder)


""" Episodes with number less than 10 should have '0' as a prefix
"""
def episode_num(num):
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)


""" Browse the TV Series folder
"""
def tv_series(path, name_list):
    print('\n\nchecking tv series...\n')

    for name in name_list:
        path_check(path, name)
        if name == 'Gotham Season 4':
            dir_contents = [ep.split('.')[1][-2:] for ep in os.listdir(path + name)]
            dir_contents.sort(key=int)
            new_ep = episode_num(1 if os.listdir(path + name) == [] else int(dir_contents[-1]) + 1)
            check('tv', name, 'http://dl.funsaber.net/serial/Gotham/season%204/720x265/', 'Gotham.S04E'+new_ep+'.720p.HDTV.2CH.x265.HEVC.Funsaber_Net.mkv')


""" Browse the Anime folder
"""
def anime(path, name_list):
    print('\n\nchecking anime...\n')

    for name in name_list:
        path_check(path, name)
        dir_contents = [ep.split('.')[0] for ep in os.listdir(path + name)]
        dir_contents.sort(key=int)
        new_ep = '1' if os.listdir(path + name) == [] else str(int(dir_contents[-1]) + 1)
        check('anime', name, 'http://www.chia-anime.tv/episode/' + name.lower().replace(' ', '-') + '/',
              'Episode ' + new_ep)


if __name__ == '__main__':
    if not is_internet_connected():
        print('No internet connection')
        sys.exit(0)

    tv_list = ['Gotham Season 4']
    anime_list = ['Boruto Naruto Next Generations', 'Dragon Ball Super']

    path_anime = '/media/shan/Local Disk/Anime/'
    path_tv = '/media/shan/Local Disk/TV/'

    tv_series(path_tv, tv_list)
    anime(path_anime, anime_list)

