import os
import subprocess

from pytube import YouTube


def download_tube_link(url, PARAMS):
    # Create YouTube url object
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

    if (PARAMS['MODE_VIDEO'] is False):
        stream = yt.streams.filter(only_audio=True).first()
        print("Downloading music only ... ")
    else:
        # Original video resolution “720p”, “480p”, “360p”, “240p”,“144p”
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        print("Downloading video ... ")
        if PARAMS['FILE_RESOLUTION']:
            stream = stream.get_by_resolution(PARAMS['FILE_RESOLUTION'])
            if stream is None:
                print(f"Defined resolution failed, trying default largest")
                stream = yt.streams.filter(progressive=True, file_extension='mp4')
                stream = stream.order_by('resolution').first()
        else:            
            stream = stream.order_by('resolution').first()
        #stream = yt.streams.filter(file_extension=FILE_EXT).first()#.get_by_resolution(FILE_RESOLUTION).first()

    
    if (os.path.exists(PARAMS['PATH_OUTPUT']) is False):
        os.makedirs(PARAMS['PATH_OUTPUT'])

    os.chdir(PARAMS['PATH_OUTPUT'])

    # Download to the indicated path with youtube title as file name
    out_file = stream.download(PARAMS['PATH_OUTPUT'])
    print(f"File downloaded locally to {PARAMS['PATH_OUTPUT']}")

    # Convert to mp3 if ffmpeg installed
    # from command line: ffmpeg -i name.mp4 file.mp3
    if (PARAMS['FILE_EXT'] == "mp3") and (PARAMS['MODE_VIDEO'] is False):
        base, ext = os.path.splitext(out_file)
        subprocess.run([
            'ffmpeg',
            '-i', 
            os.path.join(PARAMS['PATH_OUTPUT'], out_file),
            os.path.join(PARAMS['PATH_OUTPUT'], base + '.' + PARAMS['FILE_EXT'])
            ])

        # Delete mp4
        os.remove(os .path.join(PARAMS['PATH_OUTPUT'], out_file))

