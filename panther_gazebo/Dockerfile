FROM osrf/ros:galactic-desktop

# Use bash instead of sh
SHELL ["/bin/bash", "-c"]

# Update Ubuntu Software repository
RUN apt update \
    && apt upgrade -y

RUN apt install -y \
    ros-$ROS_DISTRO-xacro \
    ros-$ROS_DISTRO-geographic-msgs \
    ros-$ROS_DISTRO-joint-state-publisher \
    ros-$ROS_DISTRO-gazebo-ros-pkgs \
    ros-$ROS_DISTRO-geometry2

WORKDIR /app

# Create and initialise ROS workspace
RUN mkdir -p ros2_ws/src
RUN git clone https://github.com/husarion/panther_description.git --branch=ros2-gazebo \
    && git clone https://github.com/tu-darmstadt-ros-pkg/hector_gazebo.git --branch=foxy-devel ros2_ws/src/hector_gazebo

COPY ./panther_gazebo ros2_ws/src/panther_gazebo

RUN cd ros2_ws \
    && source /opt/ros/$ROS_DISTRO/setup.bash \
    && colcon build --symlink-install

# Clear 
RUN apt clean \
    && rm -rf /var/lib/apt/lists/* 

COPY ./ros_entrypoint.sh /