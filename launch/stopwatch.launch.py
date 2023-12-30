# SPDX-FileCopyrightText: 2023 Ryotaro Karikomi
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
  
  talker = launch_ros.actions.Node(
    package='stopwatch',
    executable='talker',
    )
  listener = launch_ros.actions.Node(
    package='stopwatch',
    executable='listener',
    output='screen'
    )

  return launch.LaunchDescription([talker, listener])