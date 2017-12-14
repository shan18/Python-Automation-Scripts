""" This module checks if a new episode is available.
"""

import requests


def episode_check(tv_anime, series_name, page_url, episode_name):
    try:
        req = requests.get(page_url)
    except Exception:
        print(tv_anime)
        print('Failed to establish a connection with the website')
        return

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
