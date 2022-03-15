import rclpy # ROS2 の Python モジュールをインポートする
from rclpy.node import Node # rclpy.node モジュールから Node クラスをインポート

def main(): # main 関数
    rclpy.init() # 初期化
    node = Node('hello_node') # ノードの生成 

    while rclpy.ok(): # CTRL+Cキーが押されるまで無限ループ
        print("hello world") # 端末に出力

    rclpy.spin(node) # ノードの実行
    node.destroy_node() # ノードの破壊
    rclpy.shutdown() # 終了処理
