from typing import Optional

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from utils.ytube_download import yt_download

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    """"
    display home page
    """
    return templates.TemplateResponse("index.html", 
                                      {"request": request, 
                                       "title": "Ytube download"})


@app.post("/download", response_class=HTMLResponse)
def download(request: Request,
             url: Optional[str] = Form(None),
             video: str = Form(...),
             quality: str = Form(...)
             ):    
    
    response = templates.TemplateResponse("index.html", {"request": request, 
                                                     "url": url, 
                                                     "title": "Ytube download"})
    
    print(f'URL {url}, video: {video}, quality: {quality}')

    # Called download function
    if url:
        path_downloads = yt_download(url, video = video, quality = quality)
        response = templates.TemplateResponse("index.html", {"request": request, 
                                                     "url": url, 
                                                     "path_downloads": path_downloads, 
                                                     "title": "Ytube download"})
    else:
        response = templates.TemplateResponse("index.html", {"request": request, 
                                                     "url": url, 
                                                     "title": "Ytube download"})
        
    return response