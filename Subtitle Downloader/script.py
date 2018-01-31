import sys
import os
import hashlib
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
    name, ext = os.path.splitext(file_path)
    if ext not in [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp",".3g2"]:
        return

    subtitle_name = name + '.srt'
    if not os.path.exists(subtitle_name):
        headers = {'User-Agent': 'SubDB/1.0 (subtitle-download/1.0; https://github.com/shan18/)'}
        url = 'http://sandbox.thesubdb.com/?action=download&hash=' + get_hash(file_path) + '&language=en'
        req = urllib.request.Request(url, None, headers)
        content = urllib.request.urlopen(req).read()

        with open(subtitle_name, 'wb') as subtitle:
            subtitle.write(content)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Atleast one parameter required')
        sys.exit(1)

    video_path = sys.argv[1]
    subtitle_download(video_path)
