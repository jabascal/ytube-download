# Target directory 
dir_target=/home/$USER/Music/downloads

# Volume directory
dir_volume=/var/lib/docker/volumes/ytube-download_ytube/_data/

# Create if directory does not exist
if [ ! -d "$dir_target" ]; then
  mkdir -p "$dir_target"
fi

# Copy files from docker volume to target directory
sudo cp -r $dir_volume $dir_target

# Move files to /downloads
sudo mv "$dir_target"/_data/* "$dir_target"

# Change permissions
sudo chmod -R a+rwx "$dir_target"

# Remove temporary directory
sudo rm -r "$dir_target"/_data