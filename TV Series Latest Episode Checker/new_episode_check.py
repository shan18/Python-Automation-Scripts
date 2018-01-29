""" This module checks if a new episode is available.
"""

from utils import get_soup


def tv_episode_check(series_name, season_num, base_url, episode_num):
    page_url = base_url + 'List_of_' + '_'.join(series_name.split()) + '_episodes'
    soup = get_soup(page_url)

    body = soup.find('div', {'class': 'mw-body', 'id': 'content'})
    body_content = body.find('div', {'class': 'mw-body-content', 'id': 'bodyContent'})
    tables = body_content.find_all(
        'table', {'class': 'wikitable plainrowheaders wikiepisodetable'}
    )  # list of tables of all the seasons
    ep_list = tables[season_num - 1].find_all('tr', {'class': 'vevent'})  # episode list for required season

    if len(ep_list) >= episode_num:
        episode_viewers = ep_list[episode_num - 1].find_all('td')[-1].text  # data from a specific episode row
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
    soup = get_soup(page_url)

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
