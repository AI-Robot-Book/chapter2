import rclpy  # 1. ROS2 の Python モジュールをインポートする
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート


def main():  # main 関数
    rclpy.init()               # 2. 初期化
    node = Node('happy_node')  # 3. ノードの生成
    while rclpy.ok():          # CTRL+Cキーが押されるまで無限ループ
        print("happy world")   # 端末に出力
    rclpy.spin(node)           # 4. ノードの実行
    node.destroy_node()        # 5. ノードの破壊
    rclpy.shutdown()           # 6. 終了処理