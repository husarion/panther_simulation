## panther_gazebo

Dockerized package containing Gazebo simulation of Panther robot.

## Hardware configurations

Depending on your hardware configuration your *docker-compose.yaml* file may differ. For Intel and AMD users you will need following *docker-compose.yaml* configuration:
``` yaml
version: '3.4'

services:
  panther_gazebo:
    image: husarion/panther-gazebo:galactic-latest
    environment:
      - "DISPLAY"
      - "QT_X11_NO_MITSHM=1"
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
    command: ros2 launch panther_gazebo panther.launch.py
```

Nvidia users have to install `nvidia-docker2`. Installation steps can be found [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html). With `nvidia-docker2` installed following *docker-compose.yaml* will be needed:

``` yaml
version: '3.4'

services:
  panther_gazebo:
    image: husarion/panther-gazebo:galactic-latest
    runtime: nvidia
    environment:
      - "DISPLAY"
      - "QT_X11_NO_MITSHM=1"
      - NVIDIA_VISIBLE_DEVICES=all
      - NVIDIA_DRIVER_CAPABILITIES=compute,utility,display
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
    command: ros2 launch panther_gazebo panhter.launch.py use_gpu:=true
```

## Launch files

### <span>panther_spawn_robot.launch</span>.py
Spawns panther model in Gazebo world and starts `robot_state_publisher` node.
#### params
  - `pos_x` (*default: 0.0*) - x coordinate of spawnpoint.
  - `pos_y` (*default: 0.0*) - y coordinate of spawnpoint.
  - `pos_z` (*default: 3.5*) - z coordinate of spawnpoint.
  - `panther_common_props_path` (*default: $(find panther_description)/models/panther/config/panther_common.yaml*) - path to file with panther common phisical parameters.
  - `wheel_props_path` (*default: $(find panther_description)/models/panther/config/WH01.yaml*) - path to file with panther wheel definition.
  - `use_gpu` (*default: false*) - enables GPU support in robot model.


  ### <span>panther_rviz2.launch</span>.py
Starts RViz2.

  ### <span>panther_world.launch</span>.py
Starts Gazebo and loads world file.
#### params
  - `world` (*default: $(find panther_description)/worlds/willowgarage.world*) - path to file with Gazebo world.
  - `use_sim_time` (*default: true*) - sets `use_sim_time` to given value.


### <span>panther.launch</span>.py
Launches all above launch files. Be default this file spawns robot in location `x` = 8.0.
#### params
  - `world` (*default: $(find panther_description)/worlds/willowgarage.world*) - path to file with Gazebo world.
  - `panther_common_props_path` (*default: $(find panther_description)/models/panther/config/panther_common.yaml*) - path to file with panther common phisical parameters.
  - `wheel_props_path` (*default: $(find panther_description)/models/panther/config/WH01.yaml*) - path to file with panther wheel definition.
  - `use_gpu` (*default: false*) - enables GPU support in robot model.

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