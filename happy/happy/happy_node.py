import rclpy  # 1. ROS2 の Python モジュールをインポートする


def print_happy(node):
    node.get_logger().info("happy world")


def main():  # main 関数
    print("Program start")
    rclpy.init()               # 2. 初期化
    node = rclpy.create_node('happy_node')  # 3. ノードの生成
    print("Create a node")
    print_happy(node)          # 4.
    node.destroy_node()        # 5. ノードの破壊
    print("Destory the node")
    rclpy.shutdown()           # 6. 終了処理
    print("Program end")
