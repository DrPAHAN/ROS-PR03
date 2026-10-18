import unittest

from patrol.patrol_node import get_command
from turtlesim_msgs.msg import Pose


class TestPatrolLogic(unittest.TestCase):

    def test_no_pose_command(self):
        # Если поза не получена, команда должна быть нулевой
        cmd = get_command(None)
        self.assertEqual(cmd.linear.x, 0.0)
        self.assertEqual(cmd.angular.z, 0.0)

    def test_with_pose_command(self):
        # Если поза получена, команда должна быть заданной
        mock_pose = Pose()
        mock_pose.x = 5.0
        mock_pose.y = 5.0
        cmd = get_command(mock_pose)
        self.assertEqual(cmd.linear.x, 0.5)
        self.assertEqual(cmd.angular.z, 0.3)


if __name__ == '__main__':
    unittest.main()
