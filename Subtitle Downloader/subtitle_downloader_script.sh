#!/usr/bin/env bash

IFS_BAK=$IFS
IFS="
"

for line in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS; do
    cd ~/
    python3 subtitle_downloader.py $line
    notify-send "Downloaded subtitle for "$line
done

IFS=$IFS_BAK
