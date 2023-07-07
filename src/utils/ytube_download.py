# Uses https://github.com/yt-dlp/yt-dlp
# yt-dlp A youtube-dl fork with additional features and fixes

import os
from pathlib import Path

import yt_dlp

url = "https://www.youtube.com/watch?v=LCJblaUkkfc"
video = "music"
quality = "first"

path_cwd = os.getcwd()
path_downloads = os.path.abspath(Path("./downloads"))
#path_downloads = os.path.abspath(Path("./"))

if (os.path.exists(path_downloads) is False):
    os.makedirs(path_downloads)
    print(f"Created path {path_downloads}")


def yt_download(url: str, video, quality):    
    os.chdir(path_downloads)
    if (video == "music"):
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
            'postprocessors': [{  # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', # 'm4a'
            }]
        }        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(url)

            print(f"Downloading music only ... {url} to {path_downloads}")
    else:
        if (quality == "first"):
            # first quality
            ydl_opts = {
                'format': 'worstvideo+worstaudio/worst',
                'outtmpl': f'{path_downloads}/%(title)s.%(ext)s'
            }
            print(f"Trying lowest first")
        else:
            # Last quality
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': f'{path_downloads}/%(title)s.%(ext)s'
            }
            print(f"Trying default largest")
       
        print("Downloading video ...")       
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(url)
    os.chdir(path_cwd)

    return path_downloads

if __name__ == '__main__':
    yt_download(url, video, quality)