from ubuntu
arg DEBIAN_FRONTEND=noninteractive

run apt update
run apt-get install -y -qq \ 
    wget build-essential cmake git \
    pkg-config \
    python3-pip python3-pycurl \
    libopencv-dev libjpeg-dev libpng-dev libtiff-dev libgtk2.0-dev libatlas-base-dev \
    gfortran webp pkg-config \ 
    qt5dxcb-plugin qt5ct python3-qtpy pyqt5-dev \
    zlib1g-dev 
    
run pip3 install twisted opencv-python-headless opencv-contrib-python
