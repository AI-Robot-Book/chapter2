import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

class HappyPubSub(Node):
    def __init__(self):
        super().__init__('happy_pub_sub')
        self.pub = self.create_publisher(String, 'happy_msg', 10)
        self.sub = self.create_subscription(Int32,'number', self.callback, 10)
        self.happy_actions = ({
            1:'他の人へ親切な行動をします．',
            2:'他の人とつながる行動をします．',
            3:'健康になるために運動をします．',
            4:'マインドフルネスをします．',
            5:'新しいことに挑戦します．',
            6:'ゴールを決めて，まず１歩を踏み出します．',
            7:'レジリエンス（回復力）をつけます．',
            8:'物事の良い面を見ます．',
            9:'人は皆違っていることを受け入れます．',
            10:'皆で協力して世界を良くします．'})

    def callback(self, sub_msg):
        pub_msg = String()
        self.get_logger().info(f'Subscribe:{sub_msg.data}') 
        pub_msg.data = self.happy_actions[sub_msg.data % 10 + 1] 
        self.pub.publish(pub_msg)
        self.get_logger().info(f'Publish: {pub_msg.data}') 

def main():
    rclpy.init()
    node = HappyPubSub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()
