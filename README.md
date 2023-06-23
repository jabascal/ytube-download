# ytube download
FastAPI app to download from youtube to mp3 (music only) or mp4 (video) with highest or lowest quality. 

![](https://github.com/jabascal/ytube-download/blob/fastapi/figures/ytube_app.png)


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

There is a current error due to changes from youtube site:
```
get_throttling_function_name: could not find match for multiple
```

## Usage
Recently, Google has added a validation step, which will be executed only the first time, requiring to validate with a google account and press enter. Outputs are downloaded to *./downloads*.


Within the environment 

```
cd src
uvicorn main:app --reload
```



