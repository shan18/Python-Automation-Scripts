""" This script checks for the new episodes of any TV series or anime.
    Enter the path name accordingly.
"""

import os
import sys

from utils import is_internet_connected, path_check, zero_prefix
from new_episode_check import tv_episode_check, anime_episode_check


# Browse the TV Series folder
def tv_series(path, name_list, mode):
    print('\n\nchecking tv series...\n')

    for name in name_list:
        path_check(path, name)

        series = ' '.join(name.split()[:-2])
        season = int(name.split()[-1])
        ep_season_occurrence = 's' + zero_prefix(season) + 'e'

        dir_contents = [ep.lower() for ep in os.listdir(path + name)]
        dir_contents_idx = [ep.find(ep_season_occurrence.lower()) for ep in dir_contents]
        dir_episodes = [ep[x+4:x+6] for x, ep in zip(dir_contents_idx, dir_contents)]
        dir_episodes.sort(key=int)

        new_ep = int(1 if os.listdir(path + name) == [] else int(dir_episodes[-1]) + 1)
        tv_episode_check(
            series, season,
            'https://en.wikipedia.org/wiki/',
            mode, new_ep
        )
    print('\n###########################################################')


# Browse the Anime folder
def anime(path, name_list):
    print('\n\nchecking anime...\n')

    for name in name_list:
        path_check(path, name)

        dir_contents = [ep.split('.')[0] for ep in os.listdir(path + name)]
        dir_contents.sort(key=int)
        new_ep = int('1' if os.listdir(path + name) == [] else str(int(dir_contents[-1]) + 1))
        anime_episode_check(
            name,
            'http://www.chia-anime.tv/episode/',
            new_ep
        )
    print('\n###########################################################')


if not is_internet_connected():
    print('No internet connection')
    sys.exit(0)

tv_list = [
    'Gotham Season 4',
    'The Flash Season 4',
    'Arrow Season 6',
    'The Big Bang Theory Season 11'
]

anime_list = [
    'Boruto Naruto Next Generations',
    'Dragon Ball Super',
    'One Piece'
]

path_anime = '/media/shan/Local Disk/Anime/'
path_tv = '/media/shan/Local Disk/TV/'

modes = ['Local File', 'Timed']

tv_series(path_tv, tv_list, modes[1])
anime(path_anime, anime_list)
