sudo apt update;
sudo apt install tmux tmuxinator ranger docker.io docker curl python3-pip -y;
sudo snap install bpytop;

sudo addgroup docker; sudo usermod -aG docker $USER;
newgrp docker;

DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker};
mkdir -p $DOCKER_CONFIG/cli-plugins;
curl -SL https://github.com/docker/compose/releases/download/v2.17.2/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose;
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose;

#pip install "https://github.com/SimplyPrint/OctoPrint-Creality2xTemperatureReportingFix/archive/master.zip"
