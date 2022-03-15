import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            namespace= "turtlesim1", package='turtlesim', executable='turtlesim_node', output='screen', respawn='true',
            remappings=[('/cmd_vel', '/kame/cmd_vel')]),
        launch_ros.actions.Node(
            namespace= "turtlesim2", package='turtlesim', executable='turtlesim_node', output='screen', respawn='true',
            parameters=[{"background_b": 200}, {"background_g": 200},{"background_r": 200}]),
        launch_ros.actions.Node(
            prefix='xterm -e', namespace= "turtlesim1", package='turtlesim', executable='turtle_teleop_key', output='screen',
            on_exit=launch.actions.Shutdown()),
        launch_ros.actions.Node(
            prefix='xterm -e', namespace= "turtlesim2", package='turtlesim', executable='turtle_teleop_key', output='screen')
    ])
