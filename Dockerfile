# Use the latest Ubuntu image as the base image
FROM ubuntu:latest

# Set environment variables to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install Python, pip, Java, wget, and virtualenv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv default-jdk wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Verify the installations
RUN python3 --version && java -version

# Create and activate a virtual environment, then install Python packages
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install mediapipe numpy

# Download the pose_landmarker task model
RUN wget -O /opt/venv/pose_landmarker.task -q https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_heavy/float16/1/pose_landmarker_heavy.task

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Command to run the application (you can customize this as needed)
CMD ["python3", "./HelloWorld.py"]
