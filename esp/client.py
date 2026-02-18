import rclpy
from rclpy.node import Node
from service_interfaces.srv import Led
class client(Node):
    def __init__(self):
        super().__init__("client")
        self.cl=self.create_client(Led,'Led')
        self.data=Led.Request()
        while not self.cl.wait_for_service(1.0):
            self.get_logger().info("waiting for service")
    def call(self, a):
        self.data.a=int(a)
        future=self.cl.call_async(self.data)
        future.add_done_callback(self.callback)
    def callback(self,future):
        result=future.result()
        self.get_logger().info(str(result.success))
        rclpy.shutdown()


        
def main(args=None):
    rclpy.init(args=args)
    node=client()
    a=input(print("enter a number between 1 and 0"))
    node.call(a)
    rclpy.spin(node)
    
    
if  __name__=="__main__":
    main()