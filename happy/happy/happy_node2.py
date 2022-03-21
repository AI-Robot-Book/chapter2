import rclpy  # 1. ROS2 Python モジュールのインポート
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート


class HappyNode(Node):
    def __init__(self):
        super().__init__('happy_node2') # 基底クラスコンストラクタのよび出し
        self.get_logger().info("happy world2") # ノードの処理


def main():  # main 関数
    print("プログラム開始")
    rclpy.init()               # 2. 初期化
    node = HappyNode()         # 3. ノードの生成
    print("ノードの生成")     
    node.destroy_node()        # 5. ノードの破壊
    print("ノードの破壊")
    rclpy.shutdown()           # 6. 終了処理
    print("プログラム終了")
