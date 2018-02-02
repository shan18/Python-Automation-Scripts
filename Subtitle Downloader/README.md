# Subtitle Downloader

This script automatically downloads the english subtitles of movies.   


## Downloading automatically via Nautilus

- Place `subtitle_downloader_script.sh` in `~/.local/share/nautilus/scripts/`

- Now place `subtitle_downloader.py` in home directory. You can change the path for this script but then you would have to update the path in `subtitle_downloader_script.sh` accordingly.

- Now **Right Click** on the movie file (not the movie folder), go to **scripts** and click on the subtitle downloader script.

- Wait for a few seconds and the subtitle will be downloaded.


### Downloading via running the python script manually
 
- To download subtitles for a single movie  
`python script.py "path_to_movie_file"`

- To download subtitles for multiple files  
`python script.py <path_to_files>`

- To download subtitles for all the movies located within a directory  
`python script.py "path_to_directory"`
