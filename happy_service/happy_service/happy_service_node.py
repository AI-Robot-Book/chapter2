from happy_interfaces.srv import AddHappy
import rclpy
from rclpy.node import Node


class HappyService(Node):  # ハッピーサービスクラス
    def __init__(self):
        super().__init__('happy_service')
        # サービスの生成
        self.service = self.create_service(AddHappy, 'add_happy',
                                       self.add_happy_callback)

    def add_happy_callback(self, request, response):  # コールバック関数
        response.happy_word = 'ハッピー' + request.word
        self.get_logger().info(f"リクエストが来ます\言葉: %s' % (request.word))
        return response


def main(args=None):  # main関数
    rclpy.init()
    happy_service = HappyService()
    try:
        rclpy.spin(happy_service)
    except KeyboardInterrupt:
        print("Ctrl+CLが押されました．")
    finally:
        node.destroy_node()
        rclpy.shutdown()
    rclpy.shutdown()                         
