import rclpy                         # ROS2 の Python モジュールをインポート
from rclpy.node import Node          # rclpy.node モジュールから Node クラスをインポート
from geometry_msgs.msg import Twist  # Twist メッセージ型をインポート


# キー操作により速度指令値をパブリッシュするクラス
class TeleopPublisher(Node):
    # コンストラクタ
    def __init__(self):
        # 基底クラスコンストラクタのよび出し．ノードの生成．
        super().__init__('teleop_publisher_node')

        # パブリッシャの生成
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        # タイマーの生成
        self.timer = self.create_timer(0.01, self.timer_callback)

        # Twist メッセージ型インスタンスの生成
        self.vel = Twist()
        self.vel.linear.x = 0.0
        self.vel.angular.z = 0.0
        print("Input f, b, r, l key, then press Enter key.")

    # タイマーのコールバック関数
    def timer_callback(self):
        # キーの取得
        key = input("f:forward, b:backward, r:right, l:left, s:stop <<")

        # キーの値により並進速度や角速度を変更
        if key == 'f':
            self.vel.linear.x += 0.1
        elif key == 'b':
            self.vel.linear.x -= 0.1
        elif key == 'l':
            self.vel.angular.z += 0.1
        elif key == 'r':
            self.vel.angular.z -= 0.1
        elif key == 's':
            self.vel.linear.x = 0.0
            self.vel.angular.z = 0.0
        else:
            print("Input f, b, r, l : ")

        # 速度指令メッセージのパブリッシュ
        self.publisher.publish(self.vel)

        # 端末に速度表示
        self.get_logger().info("Velocity: Linear=%f angular=%f"
                               % (self.vel.linear.x, self.vel.angular.z))


def main(args=None):
    rclpy.init(args=args)                 # rclpy モジュールの初期化
    teleop_publisher = TeleopPublisher()  # インスタンスの生成
    rclpy.spin(teleop_publisher)          # ノードの実行
    teleop_publisher.destroy_node()       # ノードの破壊
    rclpy.shutdown()                      # rclpy モジュールの終了処理
