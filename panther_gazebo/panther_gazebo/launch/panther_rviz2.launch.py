import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    panther_description = get_package_share_directory('panther_description')
    panther_rviz_config_path = os.path.join(panther_description, 'rviz/panther.rviz')

    return LaunchDescription([
      DeclareLaunchArgument(
        name='rvizconfig',
        default_value=panther_rviz_config_path,
        description='Absolute path to rviz config file'
      ),
      
      Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
      )
    ])

