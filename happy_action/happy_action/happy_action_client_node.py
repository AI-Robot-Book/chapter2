import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from happy_action_interfaces.action import Happy

class HappyActionClient(Node):
    def __init__(self):
        super().__init__('happy_action_client')
        self._action_client = ActionClient(self, Happy, 'happy')

    def send_goal(self, action_no):
        goal_msg = Happy.Goal()
        goal_msg.action_no = action_no
        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg,
                    feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("ゴールが拒否されました．")
            return

        self.get_logger().info("ゴールが承認されました.")
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info("結果：{}".format(result.result))
        # rclpy.shutdown()
        
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info("フィードバックを受信：残り{}秒".format(feedback.remaining_time))

def main(args=None):
    rclpy.init(args=args)
    action_client = HappyActionClient()
    action_client.send_goal(1)
    action_client.send_goal(5)
    action_client.send_goal(7)
    rclpy.spin(action_client)

if __name__ == '__main__':
    main()
