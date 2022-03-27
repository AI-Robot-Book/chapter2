# -*- coding: utf-8 -*-
import random
import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from happy_action_interfaces.action import Happy

class HappyActionServer(Node):
    def __init__(self):
        super().__init__('happy_action_server')
        self._action_server = ActionServer(
            self, Happy, 'happy', self.execute_callback)
        self.happy_actions = ({
            1:'他の人へ親切な行動をします．',
            2:'他の人とつながる行動をします．',
            3:'健康になるために運動をします．',
            4:'マインドフルネスをします．',
            5:'新しいことに挑戦します．',
            6:'ゴールを決めて，まず１歩を踏み出します．',
            7:'レジリエンス（回復力）をつけます．',
            8:'物事の良い面を見ます．',
            9:'人は皆違っていることを受け入れます．',
            10:'皆で協力して世界を良くします．'})

    def execute_callback(self, goal_handle):
        self.get_logger().info('ゴールを処理中...')

        feedback_msg = Happy.Feedback()
        feedback_msg.remaining_time = random.randrange(1,10)

        no = goal_handle.request.action_no
        self.get_logger().info(f'ゴールを受信：[{no}番] {self.happy_action[no]}')   

        
        while True:
            if  feedback_msg.remaining_time == 0:
                self.get_logger().info('ゴールの処理は終了しました．')
                break
            else:
                feedback_msg.remaining_time -= 1
                self.get_logger().info(f'フィードバック：残り{feedback_msg.remaining_time}秒')
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(1)

            
        goal_handle.succeed()
        result = Happy.Result()
        if feedback_msg.remaining_time == 0:
            result.result = 'とても幸せになりました．'
        else:
            result.result = '少し幸せになりました．'

        return result 

def main(args=None):
    rclpy.init(args=args)
    happy_action_server = HappyActionServer()
    rclpy.spin(happy_action_server)
