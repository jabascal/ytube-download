FROM python:3.8-slim-buster 

WORKDIR /usr/src/app

COPY src ./src
COPY requirements.txt README.md docker-compose.yml  Dockerfile ./

RUN apt-get -y update && \
    apt-get -y install ffmpeg && \
    apt-get -y upgrade && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

# Copy modified cipher file to avoid youtube stream error
#COPY cipher.py /usr/local/lib/python3.8/site-packages/pytube

#ENTRYPOINT ["python", "./src/run_ytube_download.py"]
CMD ["/bin/bash"]
# Run:
#   python ./src/run_ytube_download.py