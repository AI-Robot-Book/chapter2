import sys
import rclpy
from rclpy.node import Node
from happy_interfaces.srv import AddHappy

class HappyClient(Node):
    def __init__(self):
        super().__init__('happy_client_node')
        self.cli = self.create_client(AddHappy, 'add_happy')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.req = AddHappy.Request()
            
    def send_request(self):
        self.req.word = str(sys.argv[1])
        self.future = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    happy_client = HappyClient()
    happy_client.send_request()
    while rclpy.ok():
        rclpy.spin_once(happy_client)
        if happy_client.future.done():
            try:
                response = happy_client.future.result()
            except Exception as e:
                happy_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                happy_client.get_logger().info(
                    'Reqest: %s -> Response: %s' %
                    (happy_client.req.word, response.happy_word))
            break
        
    happy_client.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
