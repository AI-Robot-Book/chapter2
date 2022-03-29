import rclpy  # 1. ROS2 Python モジュールのインポート
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート


class HappyNode4(Node):  # HappyNode5クラス
    def __init__(self):  # コンストラクタ
        print("ノードの生成")
        super().__init__('happy_node5')  # 基底クラスコンストラクタのよび出し
        self.timer = self.create_timer(1.0, self.timer_callback)  # タイマーの生成

    def timer_callback(self):  # コールバック関数
        self.get_logger().info('ハッピーワールド４')  # 端末に表示


def main():  # main 関数
    print('プログラム開始')
    rclpy.init()                # 2. 初期化
    node = HappyNode4()         # 3. ノードの生成
    try:                        # 例外処理．美しく終わるため．
        # 4. ノードの処理．コールバック関数を繰り返しよび出す．
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Ctrl+Cが押されました．')
    rclpy.shutdown()             # 5. 終了処理
    print('プログラム終了')
