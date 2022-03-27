import rclpy  # 1. ROS2 Python モジュールのインポート


def print_happy(node):  # 端末にハッピーワールドと表示
    node.get_logger().info("ハッピーワールド")


def main():  # main 関数
    print('プログラム開始')
    rclpy.init()               # 2. 初期化
    print('ノードの生成')
    node = rclpy.create_node('happy_node')  # 3. ノードの生成
    print_happy(node)          # 4. ノードの処理
    print('ノードの破壊')
    node.destroy_node()        # 5. ノードの破壊
    rclpy.shutdown()           # 6. 終了処理
    print('プログラム終了')
