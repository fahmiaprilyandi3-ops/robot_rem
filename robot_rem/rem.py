import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class RemNode(Node):
    def __init__(self):
        super().__init__('rem_node')
        self.subscription = self.create_subscription(Float32, '/jarak', self.cek_jarak, 10)

    def cek_jarak(self, msg):
        if msg.data < 30.0:
            self.get_logger().warn(f'BAHAYA! Jarak {msg.data} cm -> REM DARURAT!')
        else:
            self.get_logger().info(f'Aman ({msg.data} cm) -> Lanjut jalan.')

def main():
    rclpy.init()
    node = RemNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()