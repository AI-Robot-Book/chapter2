from happy_interfaces.srv import AddHappy
import rclpy
from rclpy.node import Node

class HappyService(Node):
    def __init__(self):
        super().__init__('happy_service')
        self.srv = self.create_service(AddHappy, 'add_happy', self.add_happy_callback) 

    def add_happy_callback(self, request, response):
        response.happy_word = 'Happy ' + request.word
        self.get_logger().info('Incoming request\nword: %s' % (request.word))
        return response

def main(args=None):
    rclpy.init(args=args)
    happy_service = HappyService()
    rclpy.spin(happy_service)
    rclpy.shutdown()
