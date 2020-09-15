#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg): 
    right = msg.ranges[0]
    left = msg.ranges[719]
    forward = msg.ranges[360]

    if (forward > 1):
        if (right < 1):
            cmd.angular.z = 0.1
        elif (left < 1):
            cmd.angular.z = -0.1
        else:
            cmd.linear.x = 0.1
            cmd.angular.z = 0
    else:
        cmd.linear.x = 0.05
        cmd.angular.z = 0.1


rospy.init_node('topics_quiz_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
cmd = Twist()
rate = rospy.Rate(2)
lascan = LaserScan()



while not rospy.is_shutdown(): 
  pub.publish(cmd)
  
  rate.sleep()