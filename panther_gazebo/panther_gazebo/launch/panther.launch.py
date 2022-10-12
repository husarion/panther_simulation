#!/usr/bin/env python3

import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
  panther_gazebo = get_package_share_directory('panther_gazebo')
  panther_description = get_package_share_directory('panther_description')
  panther_description_config_path = os.path.join(panther_description, 'config')

  wheel_config_path = LaunchConfiguration('wheel_config_path', default=os.path.join(panther_description_config_path, 'WH01.yaml'))
  use_gpu = LaunchConfiguration('use_gpu', default=False)

  return LaunchDescription([
    IncludeLaunchDescription(
      PythonLaunchDescriptionSource([panther_gazebo, '/launch/panther_world.launch.py']),
    ),

    IncludeLaunchDescription(
      PythonLaunchDescriptionSource([panther_gazebo, '/launch/panther_spawn_robot.launch.py']),
      launch_arguments = {
        'pos_x' : '0.0',
        'pos_y' : '0.0',
        'wheel_config_path' : wheel_config_path,
        'use_gpu' : use_gpu
      }.items(),
    ),

    IncludeLaunchDescription(
      PythonLaunchDescriptionSource([panther_gazebo, '/launch/panther_rviz2.launch.py'])
    ),
  ])


if __name__ == '__main__':
  generate_launch_description()