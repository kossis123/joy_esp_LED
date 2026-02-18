import rclpy
import serial
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import String
class control(Node):
    def __init__(self):
        super().__init__("en_joy")
        self.sub=self.create_subscription(Joy,"/joy",self.callback,10)
        self.pub=self.create_publisher(String,"/cmd",10)
    def callback(self,msg:Joy):
        cmd=String()
        cmd.data=str(msg.axes[0])
        self.pub.publish(cmd)
        


def main(args=None):
    rclpy.init(args=args)
    node=control()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()