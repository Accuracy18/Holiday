sudo apt update;
sudo apt install tmux tmuxinator ranger docker.io docker -y --force-yes;
sudo snap install bpytop;

sudo addgroup docker; sudo usermod -aG docker $USER;
newgrp docker;
