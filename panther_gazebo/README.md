## panther_gazebo

Dockerized package containing Gazebo simulation of Panther robot.

## Hardware configurations

Depending on your hardware configuration your *docker-compose.yaml* file may differ. For Intel and AMD users you will need following *docker-compose.yaml* configuration:
``` yaml
version: '3.4'

services:
  panther_gazebo:
    image: husarion/panther-gazebo:noetic-latest
    environment:
      - "DISPLAY"
      - "QT_X11_NO_MITSHM=1"
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
    command: roslaunch panther_gazebo panther_rviz.launch
```

Nvidia users have to install `nvidia-docker2`. Installation steps can be found [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html). With `nvidia-docker2` installed following *docker-compose.yaml* will be needed:

``` yaml
version: '3.4'

services:
  panther_gazebo:
    image: husarion/panther-gazebo:noetic-latest
    runtime: nvidia
    environment:
      - "DISPLAY"
      - "QT_X11_NO_MITSHM=1"
      - NVIDIA_VISIBLE_DEVICES=all
      - NVIDIA_DRIVER_CAPABILITIES=compute,utility,display
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
    command: roslaunch panther_gazebo panther_rviz.launch
```

## Examples
In order to run simulation inside docker you have to give it access to you X11 server and start *docker-compose*.

``` bash
cd examples/default_panhter_dockerhub
xhost local:docker
docker-compose up
```

For users with Nvidia GPU:
``` bash
cd examples/nvidia_default_panhter_dockerhub
xhost local:docker
docker-compose up
```