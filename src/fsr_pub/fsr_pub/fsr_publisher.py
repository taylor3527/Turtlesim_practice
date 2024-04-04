import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray

import Jetson.GPIO as GPIO
import time

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('FSR_Publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)

        self.FSR_RH_pin = 1
        self.FSR_RT_pin = 2
        self.FSR_LH_pin = 3
        self.FSR_LT_pin = 4

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.FSR_RH_pin, GPIO.IN)
        GPIO.setup(self.FSR_RT_pin, GPIO.IN)
        GPIO.setup(self.FSR_LH_pin, GPIO.IN)
        GPIO.setup(self.FSR_LT_pin, GPIO.IN)

    def Reading(self):
        
        RH_Reading = GPIO.input(self.FSR_RH_pin)
        RT_Reading = GPIO.input(self.FSR_RT_pin)
        LH_Reading = GPIO.input(self.FSR_LH_pin)
        LT_Reading = GPIO.input(self.FSR_LT_pin)

        RH = int(RH_Reading)
        RT = int(RT_Reading)
        LH = int(LH_Reading)
        LT = int(LT_Reading)

        return [RH, RT, LH, LT]

    def timer_callback(self, Data):
        msg = Int32MultiArray()
        msg.data = Data
        self.publisher_.publish(msg)

        self.get_logger().info('"%d" "%d" "%d" "%d"' % msg.data[0] % msg.data[1] % msg.data[2] % msg.data[3])

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    try:
        while True:

            Reading = minimal_publisher.Reading()

            minimal_publisher.timer_callback(Reading)

            time.sleep(0.1)

    except KeyboardInterrupt:

        GPIO.cleanup()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
