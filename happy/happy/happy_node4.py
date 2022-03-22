import rclpy  # 1. ROS2 Python モジュールのインポート
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート


class HappyNode4(Node):  # HappyNode4クラス
    def __init__(self):  # コンストラクタ
        print("ノードの生成")
        super().__init__('happy_node4')  # 基底クラスコンストラクタのよび出し
        self.timer = self.create_timer(1.0, self.timer_callback)  # タイマーの生成

    def timer_callback(self):  # タイマーのコールバック関数
        self.get_logger().info("ハッピーワールド４")


def main():  # main 関数
    print("プログラム開始")
    rclpy.init()               # 2. 初期化
    node = HappyNode4()        # 3. ノードの生成
    rclpy.spin(node)           # 4. ノードの処理．コールバック関数を繰り返しよび出す．
    print("ノードの破壊")
    node.destroy_node()        # 5. ノードの破壊
    rclpy.shutdown()           # 6. 終了処理
    print("プログラム終了")
