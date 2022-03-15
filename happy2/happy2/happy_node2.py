import rclpy                 # ROS2 の Python モジュールをインポートする
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート
import time                  # スリープに使用する time モジュールのインポート


class HappyNode2(Node):  # HappyNode2 クラス．基底クラス Node を継承した派生クラス．
    def __init__(self):  # コンストラクタ
        super().__init__('happy_node2')  # 基底クラスのコンストラクタをよび出し
        self.print_hello()               # print_hello メソッドのよび出し

    def print_hello(self):         # メソッド
        while True:                # 無限ループ
            print("happy world2")  # 端末に出力
            time.sleep(1)          # 1 秒間スリープ


def main():              # main 関数
    rclpy.init()         # 初期化
    node = HappyNode2()  # ノードの生成
    rclpy.spin(node)     # ノードの実行
    node.destroy_node()  # ノードの破壊
    rclpy.shutdown()     # 終了処理