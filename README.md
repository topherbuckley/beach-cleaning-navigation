# beach-cleaning-navigation
AI navigation for beach cleaning robot based in Okinawa, Japan

# Docker
## Installing docker
Taken from [here](https://docs.docker.com/engine/install/ubuntu/):
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
```
sudo docker run hello-world
```
## Installing the Nvdia Container Toolkit
Taken from [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html):
```
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```
```
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
```
```
sudo nvidia-ctk runtime configure --runtime=docker \
sudo systemctl restart docker \
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json \
systemctl --user restart docker \
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```
## Building the container
`sudo docker image build -f Dockerfile -t beach-cleaning-navigation .`
## Running the container
`sudo docker container run -it --runtime=nvidia --gpus all -v /sys:/sys --device /dev/gpiochip0 -e JETSON_MODEL_NAME=JETSON_ORIN_NANO beach-cleaning-navigation /bin/bash`
