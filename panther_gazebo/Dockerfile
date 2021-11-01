FROM osrf/ros:noetic-desktop-full

# Use bash instead of sh
SHELL ["/bin/bash", "-c"]

# Update Ubuntu Software repository
RUN apt update \
    && apt upgrade -y

RUN apt install -y git \
    python3-dev \
    python3-pip \
    python3-rospkg \
    ros-$ROS_DISTRO-ros-control \
    ros-$ROS_DISTRO-ros-controllers \
    ros-$ROS_DISTRO-joint-state-publisher \
    ros-$ROS_DISTRO-hector-gazebo-plugins

# Python 3 dependencies
RUN pip3 install \
        rosdep \
        rospkg 

WORKDIR /app

# Create and initialise ROS workspace
RUN mkdir -p ros_ws/src
COPY ./panther_gazebo ros_ws/src/panther_gazebo
COPY ./panther_description ros_ws/src/panther_description
# RUN git clone https://github.com/husarion/panther_description.git --branch=dev \
#     && mv /panther_description/panther_description /ros_ws/src/panther_description \
#     && rm -rf /panther_description


RUN cd ros_ws \
    && mkdir build \
    && source /opt/ros/$ROS_DISTRO/setup.bash \
    && rosdep update \
    && rosdep install --from-paths src --ignore-src -r -y \
    && catkin_make install

# Clear 
RUN apt clean \
    && rm -rf /var/lib/apt/lists/* 

COPY ./ros_entrypoint.sh /