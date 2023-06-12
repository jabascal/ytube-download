# Copy list_links.txt to ./data
# Then, execute
cp data/list_links.txt /var/lib/docker/volumes/ytube-download_data/_data/
docker compose run ytube 

# Then execute:
# python src/run_ytube_download.py params.url_list=list_links.txt

