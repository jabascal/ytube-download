#!/usr/bin/bash

# Copy files from docker volume to local dir
PATH_DOWNLOAD="/home/$USER/Music/downloads"
if [ ! -d "$PATH_DOWNLOAD" ]
then
    mkdir -p "$PATH_DOWNLOAD"
    echo "Path '$PATH_DOWNLOAD' created!"
fi

cp -r /var/lib/docker/volumes/ytube-download_music/_data/* $PATH_DOWNLOAD