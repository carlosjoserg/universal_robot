# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    urdf = os.path.join(get_package_share_directory('ur_e_description'),
                        'urdf', 'ur3e_robot.urdf')
    rviz_config = os.path.join(get_package_share_directory('ur_e_description'),'cfg','view_robot.rviz2')
    return LaunchDescription([
        Node(package='robot_state_publisher', node_executable='robot_state_publisher', arguments=[urdf], output='screen'),
        Node(package='rviz2', node_executable='rviz2', arguments=[rviz_config], output='screen')
    ])

#        Node(package='joint_state_publisher', node_executable='joint_state_publisher', arguments=[urdf], parameters=[{'use_gui': True, }], output='screen'),