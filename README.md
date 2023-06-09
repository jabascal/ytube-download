# ytube download
Download from youtube to mp3 (music only) or mp4 (video) with desired quality. 

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
Recently, Google has added a validation step, which will be executed only the first time, requiring to validate with a google account and press enter.


### Python
In a python environment, to download music-only mp3 file, run 

```
python src/run_ytube_download.py
```
which will prompt the youtube link and will download the file to *./outputs*.

The following arguments can be passed:
- video Y : To download video; otherwise, it downloads music only on mp3
- resolution 720: 720p, 360p, ... Otherwise or if not exist, it will download the largest resolution
- format mp4 : mp4, mp3, ...

For instance, to download video format at resolution 1080p: 
```
python run_ytube_download.py --video Y --resolution 1080p
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


#### Buid the Docker image
If you want to rebuild the docker image, using the Dockerfile:

```
docker build -t juanabascal/ytube:latest .
```



