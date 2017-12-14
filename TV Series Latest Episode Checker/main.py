#!/usr/bin/env python3

""" This script checks for the new episodes of TV series and anime and gives the download link
    Enter the path name and the url of the website accordingly.
"""

import os
import sys

from .prerequisites_check import is_internet_connected, path_check
from .new_episode_check import episode_check


# Episodes with number less than 10 should have '0' as a prefix
def episode_num(num):
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)


# Browse the TV Series folder
def tv_series(path, name_list):
    print('\n\nchecking tv series...\n')

    for name in name_list:
        path_check(path, name)
        if name == 'Gotham Season 4':
            dir_contents = [ep.split('.')[1][-2:] for ep in os.listdir(path + name)]
            dir_contents.sort(key=int)
            new_ep = episode_num(1 if os.listdir(path + name) == [] else int(dir_contents[-1]) + 1)
            episode_check(
                'tv', name,
                'http://dl.funsaber.net/serial/Gotham/season%204/720x265/',
                'Gotham.S04E'+new_ep+'.720p.HDTV.2CH.x265.HEVC.Funsaber_Net.mkv'
            )
        elif name == 'Arrow Season 6':
            dir_contents = [ep.split('.')[1][-2:] for ep in os.listdir(path + name)]
            dir_contents.sort(key=int)
            new_ep = episode_num(1 if os.listdir(path + name) == [] else int(dir_contents[-1]) + 1)
            episode_check(
                'tv', name,
                'http://dl.funsaber.net/serial/Arrow/season%206/720x265/',
                'Arrow.S04E'+new_ep+'.720p.HDTV.2CH.x265.HEVC.Funsaber_Net.mkv'
            )
        elif name == 'The Flash Season 4':
            dir_contents = [ep.split('.')[3][-2:] for ep in os.listdir(path + name)]
            dir_contents.sort(key=int)
            new_ep = episode_num(1 if os.listdir(path + name) == [] else int(dir_contents[-1]) + 1)
            episode_check(
                'tv', name,
                'http://dl.funsaber.net/serial/The%20Flash/season%204/720x265/',
                'The.Flash.2014.S04E'+new_ep+'.720p.HDTV.2CH.x265.HEVC.Funsaber_Net.mkv'
            )


# Browse the Anime folder
def anime(path, name_list):
    print('\n\nchecking anime...\n')

    for name in name_list:
        path_check(path, name)
        dir_contents = [ep.split('.')[0] for ep in os.listdir(path + name)]
        dir_contents.sort(key=int)
        new_ep = '1' if os.listdir(path + name) == [] else str(int(dir_contents[-1]) + 1)
        episode_check('anime', name, 'http://www.chia-anime.tv/episode/' + name.lower().replace(' ', '-') + '/',
              'Episode ' + new_ep)


if __name__ == '__main__':
    if not is_internet_connected():
        print('No internet connection')
        sys.exit(0)

    tv_list = ['Gotham Season 4', 'The Flash Season 4', 'Arrow Season 6']
    anime_list = ['Boruto Naruto Next Generations', 'Dragon Ball Super']

    path_anime = '/media/shan/Local Disk/Anime/'
    path_tv = '/media/shan/Local Disk/TV/'

    tv_series(path_tv, tv_list)
    anime(path_anime, anime_list)
