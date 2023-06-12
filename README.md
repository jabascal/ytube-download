# ytube download
Download from youtube to mp3 (music only) or mp4 (video) with desired quality. 

```
ytube-download
|-- data
|   |-- list_links.txt
|-- downloads
|-- src
|   |-- conf
|   |   |- __init__.py
|   |   |- config.py
|   |   |- config.yaml
|   `-- run_ytube_download.py
|   |-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- .gitignore
`-- README.md
```

## Installation
### Python
Install in a python environment:
```
pip install -r requirements.txt
```

Conversion from *mp4* to *mp3* requires *ffmpeg* to be installed. In linux:
```
sudo apt-get ffmpeg
```

### Docker
Install Docker and pull the docker image:
```
docker pull juanabascal/ytube:latest
```


## Usage
It allows to download one or more URL's as mp3 or mp4 with a desired resolution if the latter exists. 

Recently, Google has added a validation step, which will be executed only the first time, requiring to validate with a google account and press enter.


### Python
In a python environment, to download music-only mp3 file, run 

```
python src/run_ytube_download.py
```
which will prompt the youtube link and will download the file to *./downloads*.

The following arguments can be passed following [*hydra*](https://hydra.cc/docs/intro/) framework:
- params.video = Y : To download video; otherwise, it downloads music only on mp3
- params.file_resolution = 1020p: 720p, 360p, ... Otherwise or if not exist, it will download the largest resolution
- params.file_ext = mp4 : mp4, mp3, ...

For more information on hydra, refer to [netune.ai/blog](https://neptune.ai/blog/how-to-manage-track-visualize-hyperparameters).

For instance, to download video format at resolution 1080p: 
```
python src/run_ytube_download.py params.video=Y params.fileresolution=1080p
```

To download a list of URLs, place a txt file with the list of URLs in the folder *./data/* and execute:
```
python src/run_ytube_download.py params.url_list=list_links.txt
```

### Docker
To run with Dockerfile, pass the volume, and then excecute the python program: 
```
docker run --rm -i -t -v music:/usr/src/app/outputs juanabascal/ytube:latest
python src/run_ytube_download.py
```
Music is downloaded to the */ytube-download_music* volume at */var/lib/docker/volumes/ytube-download_music/_data/*. 

To run with docker-compose.yml:
```
docker compose run ytube
python src/run_ytube_download.py
```
Music is downloaded to the *music* volume at */var/lib/docker/volumes/music/_data/*. 
To copy files to local directory:
```
chmod +x copy_downloads.sh
./copy_downloads.sh
```


To use the text file with list of URLs, you can run *ytube_song_list.sh* 


