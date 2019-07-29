# Dockerizer
Isolate and speed up the implementation of a new repo. Stop polluting your host machine with random packages!

![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fgithub.com%2Fenric1994%2Fdocker)
## Usage

1. Clone the Dockerizer in the same folder where the code is:
`git clone https://github.com/enric1994/docker.git`
2. Add all the Python dependencies into **docker/requirements.txt** and the OS dependencies in **docker/requirements_os.txt**
3. Start Dockerizer
  ```
  cd docker
  make run
  ```
4.Jump inside the evironment:
`make dev`

**Note: Remove the .git folder before pushing to other repository!**: `rm -rf docker/.git`

## Alias
Set this alias to automatically clone and remove the docker/.git:

`alias dockerize='git clone https://github.com/enric1994/docker.git; rm -rf docker/.git'`

## Other commands
* Rebuild the container after modifying the image: `make build`
* Turn off the container: `make down`
* Check the status of the container: `make status`
* Visualize the logs: `make logs`

## Dependencies
* [Docker and Docker Compose](https://gist.github.com/enric1994/3b5c20ddb2b4033c4498b92a71d909da)
* [NVIDIA-Docker](https://github.com/NVIDIA/nvidia-docker#quickstart) (Optional, GPU required)
