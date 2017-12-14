""" This module is used to download the episodes.
"""

import requests


# Use this function if you want to download the episode from terminal
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
