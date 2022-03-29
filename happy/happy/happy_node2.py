import rclpy  # 1. ROS2 Python モジュールのインポート
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート


class HappyNode2(Node):  # HappyNode2クラス
    def __init__(self):
        print('ノードの生成')
        super().__init__('happy_node2')  # 基底クラスコンストラクタのよび出し
        self.get_logger().info('ハッピーワールド２')  # ノードの処理


def main():  # main 関数
    print('プログラム開始')
    rclpy.init()               # 2. 初期化
    node = HappyNode2()        # 3. ノードの生成
    rclpy.shutdown()           # 5. 終了処理
    print('プログラム終了')
