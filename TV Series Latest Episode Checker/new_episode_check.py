""" This module checks if a new episode is available.
"""

import requests
from bs4 import BeautifulSoup


def get_soup_object(page_url):
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


def tv_episode_check(series_name, season_num, base_url, episode_num):
    page_url = base_url + 'List_of_' + '_'.join(series_name.split()) + '_episodes'
    soup = get_soup_object(page_url)

    body = soup.find('div', {'class': 'mw-body', 'id': 'content'})
    body_content = body.find('div', {'class': 'mw-body-content', 'id': 'bodyContent'})
    tables = body_content.find_all(
        'table', {'class': 'wikitable plainrowheaders wikiepisodetable'}
    )
    tr = tables[season_num - 1].find_all('tr', {'class': 'vevent'})

    if len(tr) >= episode_num:
        episode_viewers = tr[episode_num - 1].find_all('td')[-1].text
        if 'TBD' not in episode_viewers.upper():
            print(
                series_name +
                ' Season ' +
                str(season_num) +
                ': ' +
                'Episode ' +
                str(episode_num)
            )


def anime_episode_check(series_name, base_url, episode_num):
    page_url = base_url + '-'.join(series_name.lower().split()) + '/'
    soup = get_soup_object(page_url)

    right_col = soup.find('div', {'class': 'col-right', 'id': 'archive'})
    right_col_content = right_col.find('div', {'id': 'countrydivcontainer'})
    ep_box = right_col_content.find_all(
        'div', {'class': 'box2', 'itemprop': 'episode'}
    )
    ep_num = ep_box[0].find(
        'div', {'class': 'post'}
    ).find('h3', {'itemprop': 'episodeNumber'}).text
    ep_num_int = int(ep_num.split()[-1])

    if ep_num_int >= episode_num:
        print(
            series_name +
            ': ' +
            'Episode ' +
            str(episode_num)
        )
