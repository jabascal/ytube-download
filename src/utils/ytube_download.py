
import os
from pathlib import Path

from pytube import YouTube

url = "https://www.youtube.com/watch?v=LCJblaUkkfc"
video = "music"
quality = "first"

path_downloads = Path("./downloads")

if (os.path.exists(path_downloads) is False):
    os.makedirs(path_downloads)
    print(f"Created path {path_downloads}")

def yt_download(url: str, video, quality):
    
    # Create YouTube url object
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True) #cfg.url.url_link

    if (video == "music"):
        stream = yt.streams.filter(only_audio=True).first()
        print(f"Downloading music only ... {url} to {path_downloads}")
    else:
        print("Downloading video ...")
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        if (quality == "first"):
            # first quality
            stream = stream.order_by('resolution').first()
        else:
            # Last quality
            print(f"Trying default largest")
            stream = stream.order_by('resolution').last()
    out_file = stream.download(path_downloads)
    print(f"Downloaded !!!")

if __name__ == '__main__':
    yt_download(url, video, quality)