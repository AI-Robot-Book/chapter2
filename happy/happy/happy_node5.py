import rclpy  # 1. ROS2 Python モジュールのインポート
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート


class HappyNode5(Node):  # HappyNode5クラス
    def __init__(self):  # コンストラクタ
        super().__init__('happy_node5')  # 基底クラスコンストラクタのよび出し
        self.timer = self.create_timer(1.0, self.timer_callback)  # タイマーの生成

    def timer_callback(self):  # コールバック関数
        self.get_logger().info("ハッピーワールド５")  # 端末に表示


def main():  # main 関数
    print("プログラム開始")
    rclpy.init()                # 2. 初期化
    node = HappyNode5()         # 3. ノードの生成
    print("ノードの生成")
    try:                        # 例外処理．美しく終わるため．
        # 4. ノードの処理．コールバック関数を繰り返しよび出す．
        #    Ctrl+Cが押されるまでプログラムはここでブロックされる．
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Ctrl+Cが押されました．")
    finally:                       # 例外処理の終了時に常に行う処理
        node.destroy_node()        # 5. ノードの破壊
        print("ノードの破壊")
        rclpy.shutdown()           # 6. 終了処理
        print("プログラム終了")
