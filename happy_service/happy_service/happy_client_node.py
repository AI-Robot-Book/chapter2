import sys
import rclpy
from rclpy.node import Node
from happy_interfaces.srv import AddHappy

class HappyClient(Node):
    def __init__(self):
        super().__init__('happy_client_node')
        # クライアントの生成
        self.client = self.create_client(AddHappy, 'add_happy')
        # サービスが利用できるまで待機
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('サービスは利用できません．待機中...')
        # リクエストのインスタンス生成
        self.request = AddHappy.Request()
            
    def send_request(self):
        # リクエストに値の代入
        self.request.word = str(sys.argv[1])
        # サービスのリクエスト
        self.future = self.client.call_async(self.request)

def main(args=None):
    rclpy.init(args=args)
    happy_client = HappyClient()
    happy_client.send_request()
    while rclpy.ok():
        rclpy.spin_once(happy_client)
        if happy_client.future.done(): # サービスの処理が終了したら
            try:
                response = happy_client.future.result() # サービスの結果をレスポンスに代入
            except Exception as e:
                happy_client.get_logger().info(f"サービスのよび出しは失敗しました．{e}")
            else:
                # 結果の表示
                happy_client.get_logger().info(　
                    f"リクエスト: {happy_client.req.word} -> レスポンス: {response.happy_word}")
                break        
    happy_client.destroy_node()
    rclpy.shutdown()
