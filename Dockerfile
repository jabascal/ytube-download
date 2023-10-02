# Image as base
FROM python:3.9-slim-buster

WORKDIR /usr/app

RUN apt-get -y update && \
    apt-get -y install ffmpeg

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

RUN chmod +x run_ytube.sh

RUN ls

CMD ["./run_ytube.sh"]

