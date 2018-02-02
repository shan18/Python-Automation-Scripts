#!/usr/bin/env python

import sys
import os
import hashlib
import logging
import urllib.request


def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()


def subtitle_download(file_path):
    try:
        name, ext = os.path.splitext(file_path)
        if ext not in [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp",".3g2"]:
            logging.info(ext + ' is not a valid video format.')
            return

        subtitle_name = name + '.srt'
        if not os.path.exists(subtitle_name):
            headers = {
                'User-Agent': 'SubDB/1.0 (subtitle-download/1.0; https://github.com/shan18/Python-Automation-Scripts/)'
            }
            url = 'http://api.thesubdb.com/?action=download&hash=' + get_hash(file_path) + '&language=en'
            req = urllib.request.Request(url, None, headers)
            content = urllib.request.urlopen(req).read()

            with open(subtitle_name, 'wb') as subtitle:
                subtitle.write(content)
                logging.info('Downloaded subtitle for ' + name + ' successfully.')
        else:
            logging.info('Subtitle for ' + name + ' already exists.')
    except:
        file_name = file_path.split('/')[-1]
        print('Cannot find subtitles for', file_name)
        logging.info('Cannot find subtitles for ' + file_name)
        # print('Error', sys.exc_info())


def main():
    script, _ = os.path.splitext(sys.argv[0])
    logging.basicConfig(filename=script + '.log', level=logging.INFO)
    logging.info("Parameters given: " + str(sys.argv))

    if len(sys.argv) == 1:
        print('Atleast one parameter required')
        sys.exit(1)

    for path in sys.argv[1:]:
        if os.path.isdir(path):
            for path_name, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(path_name, file)
                    subtitle_download(file_path)
        else:
            subtitle_download(path)


if __name__ == '__main__':
    main()
