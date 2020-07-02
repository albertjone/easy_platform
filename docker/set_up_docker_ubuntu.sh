
set -o xtrace
# update
sudo apt update -y

# install a few prerequisite packages which let apt use packages over HTTPS
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y

# install a few prerequisite packages which let apt use packages over HTTPS
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add the Docker repository to APT sources
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

# sudo apt update
sudo apt update

# check the version number for Docker
echo "$(apt-cache policy docker-ce)"

# install docker
sudo apt install docker-ce -y

# enable docker
sudo systemctl enable docker

# start docker
sudo systemctl start docker

# Executing the Docker Command Without Sudo (Optional)
sudo usermod -aG docker ${USER}
