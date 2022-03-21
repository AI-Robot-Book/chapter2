import rclpy  # 1. ROS2 の Python モジュールをインポートする
from rclpy.node import Node  # rclpy.node モジュールから Node クラスをインポート

class HappyNode(Node):
    def __init__(self):
        super().__init__('happy_node2')
        self.get_logger().info("happy world2")

def main():  # main 関数
    print("Program start")
    rclpy.init()               # 2. 初期化
    node = HappyNode()  # 3. ノードの生成
    print("Create a node")
    #print_happy(node)   # 3 
  
    node.destroy_node()        # 5. ノードの破壊
    print("Destory the node")
    rclpy.shutdown()           # 6. 終了処理
    print("Program end")