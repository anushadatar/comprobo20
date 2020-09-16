#!/usr/bin/env python3
""" Investigate receiving a message using a callback function """
import rospy
from geometry_msgs.msg import PointStamped

class ReceiveMessageNode(object):
    """
    Test object that receives and prints PointStamped messages.
    """
    def __init__(self):
        rospy.init_node('receive_message')
        rospy.Subscriber("/my_point", PointStamped, self.process_point)

    def process_point(self, msg):
        print(msg.header)

    def run_node(self):
        rospy.spin()

if __name__ == '__main__':
    test_receive_node = ReceiveMessageNode()
    test_receive_node.run_node()
