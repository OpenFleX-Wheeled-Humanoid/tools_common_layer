import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('pcd2pgm'), 'config', 'pcd.yaml')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    pcd_path = LaunchConfiguration('pcd_path', default='')

    pcd2pgm_node = Node(
        package='pcd2pgm',
        executable='pcd2pgm_node',
        output='screen',
        parameters=[
            config,
            {
                'use_sim_time': use_sim_time,
                'pcd_path': pcd_path,
            }
        ]
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true'),
        DeclareLaunchArgument(
            'pcd_path',
            default_value='',
            description='Absolute path to the input PCD file; overrides file_directory/file_name',
        ),
        pcd2pgm_node,
    ])
