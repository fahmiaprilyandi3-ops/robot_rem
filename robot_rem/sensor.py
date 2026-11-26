import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.publisher_ = self.create_publisher(Float32, '/jarak', 10)
        self.timer = self.create_timer(1.0, self.kirim_jarak)

    def kirim_jarak(self):
        msg = Float32()
        msg.data = round(random.uniform(10.0, 100.0), 1)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Sensor kirim jarak: {msg.data} cm')

def main():
    rclpy.init()
    node = SensorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()