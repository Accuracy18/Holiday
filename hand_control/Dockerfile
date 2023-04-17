# Use a base image with CPU support
FROM python:3.8-slim-buster

# Install required apt packages
RUN apt-get update && apt-get install -y nmap iproute2 ncat libglib2.0-0 xcb

# Install required Python packages
RUN pip install opencv-python tensorflow mediapipe openai twisted face-detection

# Set environment variable for camera to work with bridge mode
ENV OPENCV_VIDEOIO_PRIORITY_MSMF=0
