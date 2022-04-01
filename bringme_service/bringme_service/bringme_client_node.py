import rclpy
from rclpy.node import Node
from airobot_interfaces.srv import StringCommand


class BringmeClient(Node):
    def __init__(self):
        super().__init__('bringme_client_node')
        # クライアントの生成
        self.client = self.create_client(StringCommand, 'command')
        # サービスが利用できるまで待機
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('サービスは利用できません．待機中...')
        # リクエストのインスタンス生成
        self.request = StringCommand.Request()

    def send_request(self, order):
        # リクエストに値の代入
        self.request.command = order
        # サービスのリクエスト
        self.future = self.client.call_async(self.request)


def main(args=None):
    rclpy.init(args=args)
    node = BringmeClient()
    order = input('何を取ってきますか：')
    node.send_request(order)

    while rclpy.ok():
        rclpy.spin_once(node)

        if node.future.done():  # サービスの処理が終了したら
            try:
                response = node.future.result()  # サービスの結果をレスポンスに代入                  
            except Exception as e:
                node.get_logger().info(f"サービスのよび出しは失敗しました．{e}")
            else:
                # 結果の表示
                node.get_logger().info(
                    f"\nリクエスト:{node.request.command} -> レスポンス: {response.answer}")
                break
  
    rclpy.shutdown()
