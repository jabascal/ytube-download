import os
import subprocess
from pathlib import Path

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf
from pytube import YouTube

from conf.config import YTubeConfig

cs = ConfigStore.instance()
cs.store(name="ytube_config", node=YTubeConfig)

@hydra.main(config_path="conf", config_name="config")
def download_ytube_link(cfg: YTubeConfig):
    print("Config file: ")
    print(OmegaConf.to_yaml(cfg))   

    # If list of URLs given     
    if cfg.params.url_list:
        # Read file with URLs       
        with open(os.path.join(cfg.paths.data, cfg.params.url_list), 'r') as f:
            urls = f.readlines()
    else:
        if not cfg.params.url:
            # Enter URL
            URL = input("Enter URL: ")    
            #URL = 'https://www.youtube.com/watch?v=4WWJH61DKJI'

        urls = [URL]


    for url in urls:
        # Create YouTube url object
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

        if (cfg.params.video == "N"):
            # Only audio
            stream = yt.streams.filter(only_audio=True).first()
            print("Downloading music only ... ")
        else:
            # Original video resolution “720p”, “480p”, “360p”, “240p”,“144p”
            stream = yt.streams.filter(progressive=True, file_extension='mp4')
            print("Downloading video ... ")
            if cfg.params.file_resolution:
                stream = stream.get_by_resolution(cfg.params.file_resolution)
                if stream is None:
                    print(f"Defined resolution failed, trying default largest")
                    stream = yt.streams.filter(progressive=True, file_extension='mp4')
                    stream = stream.order_by('resolution').first()
            else:            
                stream = stream.order_by('resolution').first()
            #stream = yt.streams.filter(file_extension=file_ext).first()#.get_by_resolution(file_resolution).first()
        
        if (os.path.exists(Path(cfg.paths.downloads)) is False):
            os.makedirs(Path(cfg.paths.downloads))

        # Download to the indicated path with youtube title as file name
        out_file = stream.download(Path(cfg.paths.downloads))
        print(f"File downloaded locally to {Path(cfg.paths.downloads)}")

        # Convert to mp3 if ffmpeg installed
        # from command line: ffmpeg -i name.mp4 file.mp3
        if (cfg.params.file_ext == "mp3") and (cfg.params.video == "N"):
            base, ext = os.path.splitext(out_file)
            subprocess.run([
                'ffmpeg',
                '-i', 
                out_file,
                f"{base}.{cfg.params.file_ext}"
                ])

            # Delete mp4
            os.remove(out_file)

    if ('/usr/src/app' in os.getcwd()):
        print("Results saved to /var/lib/docker/volumes/ytube-download_music/_data/")
    else:
        print(f"Results saved to {Path(cfg.paths.downloads)}")


if __name__ == '__main__':
    download_ytube_link()
