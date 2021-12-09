#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

path = []

def callback(data):
	path.append([data.linear.x, data.linear.y, data.linear.z, data.angular.x, data.angular.y, data.angular.z])
	print(path[-1])    
     
def listener():
 
     # In ROS, nodes are uniquely named. If two nodes with the same
     # name are launched, the previous one is kicked off. The
     # anonymous=True flag means that rospy will choose a unique
     # name for our 'listener' node so that multiple listeners can
     # run simultaneously.
     rospy.init_node('listener', anonymous=True)
 
     rospy.Subscriber("joy_teleop/cmd_vel", Twist, callback)
 
     # spin() simply keeps python from exiting until this node is stopped
     rospy.spin()
 
if __name__ == '__main__':
	listener()
	with open('your_file.txt', 'w') as f:
    		for item in path:
        		f.write("%s\n" %item)
