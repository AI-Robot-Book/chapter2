import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# 速度指令値のトピック cmd_vel をサブスクライブして端末に表示するたけの簡単なクラス
class MySubscriber(Node):
    # コンストラクタ
    def __init__(self):
        super().__init__('my_subscriber_node')

        # サブスクライバの生成
        self.subscription = self.create_subscription(Twist,'cmd_vel',self.callback,10)

    # コールバック関数．端末に並進と角速度を表示する
    def callback(self, Twist):
        self.get_logger().info("Velocity: Linear=%f angular=%f" % (Twist.linear.x,Twist.angular.z))

def main(args=None):
    rclpy.init(args=args)
    my_subscriber = MySubscriber()
    rclpy.spin(my_subscriber)
    my_subscriber.destory_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
