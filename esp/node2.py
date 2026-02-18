import rclpy
from rclpy.node import Node
import serial
from std_msgs.msg import String
import time
class joy(Node):
    def __init__(self):
        super().__init__("node")
        self.sub=self.create_subscription(String,'/cmd',self.callback,10)
        self.ser=serial.Serial(
            port='/dev/rfcomm0',
            baudrate=115200,
            timeout=1
        )
        time.sleep(2)
    def callback(self,msg:String):
        self.a=int(float(msg.data))
        self.get_logger().info(str(self.a))

        if self.a==1:
            self.ser.write(b"1")
        elif self.a==-1:
            self.ser.write(b"0")

        

def main():
    rclpy.init()
    node=joy()
    rclpy.spin(node)
    node.ser.close()
    rclpy.shutdown()
if __name__=="__main__":
    main()