import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            prefix='xterm -e', package='happy_topic', executable='happy_publisher_node', output='screen')
            ])

