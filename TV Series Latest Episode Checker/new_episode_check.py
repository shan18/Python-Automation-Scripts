""" This module checks if a new episode is available.
"""

from datetime import datetime, timedelta

from utils import get_soup, display


def tv_episode_check(series_name, season_num, base_url, mode, episode_num=None):
    page_url = base_url + 'List_of_' + '_'.join(series_name.split()) + '_episodes'
    soup = get_soup(page_url)

    body = soup.find('div', {'class': 'mw-body', 'id': 'content'})
    body_content = body.find('div', {'class': 'mw-body-content', 'id': 'bodyContent'})
    tables = body_content.find_all(
        'table', {'class': 'wikitable plainrowheaders wikiepisodetable'}
    )  # list of tables of all the seasons
    ep_list = tables[season_num - 1].find_all('tr', {'class': 'vevent'})  # episode list for required season

    if mode.lower() == 'local file':
        if len(ep_list) >= episode_num:
            ep_data = ep_list[episode_num - 1].find_all('td')
            ep_views = ep_data[-1].text  # data from a specific episode row
            ep_title = ep_data[1].text
            if 'TBD' not in ep_views.upper():
                display(series_name, str(season_num), str(episode_num), ep_title)
    else:
        last_release = None
        ep_num = ''
        ep_title = ''
        for ep_info in ep_list[::-1]:
            ep_data = ep_info.find_all('td')
            ep_views = ep_data[-1].text
            if ep_views.upper() != 'TBD':
                ep_num = ep_data[0].text
                ep_title = ep_data[1].text
                ep_release = ep_data[-3].text
                last_release = ep_release[ep_release.find('(') + 1:-1]
                break
        if last_release is not None:
            last_release = datetime.strptime(last_release, '%Y-%m-%d')  # convert from str to datetime
            seven_days_before = datetime.now() - timedelta(days=7)
            if seven_days_before < last_release:
                display(series_name, str(season_num), ep_num, ep_title)


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
