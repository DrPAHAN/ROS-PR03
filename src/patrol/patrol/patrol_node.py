from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from turtlesim_msgs.msg import Pose


def get_command(last_pose: Pose | None) -> Twist:
    msg = Twist()
    if last_pose is None:
        msg.linear.x = 0.0
        msg.angular.z = 0.0
    else:
        msg.linear.x = 0.5
        msg.angular.z = 0.3
    return msg


class PatrolNode(Node):

    def __init__(self):
        super().__init__('patrol')
        self.last_pose = None

        self.pose_sub = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        self.cmd_pub = self.create_publisher(Twist, 'cmd_vel', 10)

        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('Нода patrol запущена и ожидает позу...')

    def pose_callback(self, msg: Pose):
        self.last_pose = msg

    def timer_callback(self):
        cmd = get_command(self.last_pose)
        self.cmd_pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = PatrolNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
