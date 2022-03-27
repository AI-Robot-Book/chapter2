import rclpy
from rclpy.node import Node
from happy_interfaces.srv import AddHappy  # サービスファイルからAddHappy型をインポート


class HappyService(Node):  # ハッピーサービスクラス
    def __init__(self):  # コンストラクタ
        super().__init__('happy_service')
        # サービスの生成（サービス型，サービス名, コールバック関数)
        self.service = self.create_service(AddHappy, 'add_happy',
                                           self.add_happy_callback)

    def add_happy_callback(self, request, response):  # コールバック関数
        response.happy_word = 'Happy ' + request.word
        self.get_logger().info(f"リクエストが来ます．ワード: {request.word}")
        return response


def main():  # main関数
    rclpy.init()
    happy_service = HappyService()
    try:
        rclpy.spin(happy_service)
    except KeyboardInterrupt:
        print("Ctrl+CLが押されました．")
    finally:
        happy_service.destroy_node()
        rclpy.shutdown()
    rclpy.shutdown()
