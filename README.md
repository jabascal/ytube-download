# ytube download
Download from youtube to mp3 (music only) or mp4 (video) with desired quality. 

# Installation
Install in a python environment:
```
pip install -r requirements.txt
```

Conversion from *mp4* to *mp3* requires *ffmpeg* to be installed. In linux:
```
sudo apt-get ffmpeg
```

# Usage
Recently, Google has added a validation step, which will be executed only the first time, requiring to validate with a google account.

To download music-only mp3 file, run 

```
python run_ytube_download.py
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




