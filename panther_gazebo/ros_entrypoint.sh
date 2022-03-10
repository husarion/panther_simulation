#!/bin/bash
set -e

export RMW_IMPLEMENTATION=rmw_fastrtps_cpp

# setup ros environment
source "/opt/ros/$ROS_DISTRO/setup.bash"
source "/app/ros2_ws/install/setup.bash"
source "/usr/share/gazebo/setup.sh"

exec "$@"