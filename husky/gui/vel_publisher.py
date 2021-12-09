#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


with open("your_file.txt", "r") as f:
	a = f.read()
	b = a.split("\n")
	b.pop()
	for i in range (len(b)):
		b[i] = b[i].strip("[")
		b[i] = b[i].strip("]")

	for i in range (len(b)):
		b[i] = b[i].split(",")

	for i in range (len(b)):
		for j in range (len(b[i])):
			b[i][j] = float((b[i][j]))

def talker():
	pub = rospy.Publisher("joy_teleop/cmd_vel", Twist, queue_size = 10)
	rospy.init_node('vel_publisher', anonymous=True)
	rate = rospy.Rate(10)
	while b:
		temp = b.pop(0)
		msg =  Twist()
		msg.linear.x = temp[0]
		msg.linear.y = temp[1]
		msg.linear.z = temp[2]
		msg.angular.x = temp[3]
		msg.angular.y = temp [4]
		msg.angular.z = temp[5]
		print(msg)

		pub.publish(msg)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
