import rclpy  # 1. ROS2 Python モジュールのインポート
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート


class HappyNode(Node):   # HappyNodeクラス
    def __init__(self):  # コンストラクタ
        super().__init__('happy_node2')  # 基底クラスコンストラクタのよび出し
        self.timer = self.create_timer(1.0, self.timer_callback) # タイマーの生成

    def timer_callback(self): # タイマーのコールバック関数
        self.get_logger().info("ハッピーワールド３")


def main():  # main 関数
    print("プログラム開始")
    rclpy.init()               # 2. 初期化
    node = HappyNode()         # 3. ノードの生成
    print("ノードの生成")
    rclpy.spin_once(node)      # 4. ノードの処理．コールバック関数のよび出し
    node.destroy_node()        # 5. ノードの破壊
    print("ノードの破壊")
    rclpy.shutdown()           # 6. 終了処理
    print("プログラム終了")
