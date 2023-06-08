import argparse
import os

from utils.helpers import download_tube_link

# ARGUMENTS
parser = argparse.ArgumentParser(description = "Download youtube link as mp3 or mp4")
parser.add_argument("-u", "--url", type=str, help="Youtube url")
parser.add_argument("-f", "--format", type=str, help="Saved format: 'mp4', 'mp3'")
parser.add_argument("-v", "--video", type=str, choices=["Y","N"], help="Video: Y, N")
parser.add_argument("-r", "--resolution", type=str, help="Resolution: 720p, 360p")
args = parser.parse_args()
print(args)

# PARAMETERS
PARAMS = {
    'PATH_OUTPUT': os.path.abspath('./outputs'), 
    'MODE_VIDEO': False,
    'FILE_RESOLUTION': None,
    'FILE_EXT': 'mp3'
}

if args.url:
    URL = args.url
else:
    # Enter URL
    URL = input("Enter URL: ")    
if args.format:
    PARAMS['FILE_EXT'] = args.format
if args.video == "Y":
    PARAMS['MODE_VIDEO'] = True
    PARAMS['FILE_EXT'] = 'mp4'
    print(f"Mode video {PARAMS['MODE_VIDEO']}")
if args.resolution:
    PARAMS['FILE_RESOLUTION'] = args.resolution  
    print(f"Resolution set to {PARAMS['FILE_RESOLUTION']}")  

if __name__ == '__main__':
    download_tube_link(url=URL, PARAMS=PARAMS)
