#!/usr/bin/env python
import subprocess
import gc
import rospy
import os 
from std_msgs.msg import String
import geometry_msgs.msg
from rosgraph_msgs.msg import Clock


popen = subprocess.Popen("gzclient -g libsystem_gui.so".split(),stdout=subprocess.PIPE)	
x =0.0
y = 0.0
z = 0.0


def listener():

	rospy.init_node('listener', anonymous=True)
	a =rospy.wait_for_message("clock", Clock)
	b = str(a).split(":")
	return(int(b[3]), int(b[2][:5]))

while True:
	try:
		for line in iter(popen.stdout.readline,""):	
				line_s = line.split()
				x = float(line_s[3])
				y = float(line_s[4])
				z = float(line_s [5])
				nsec, sec = listener()
				
				cmd2 = "rostopic pub -1 /move_base_simple/goal geometry_msgs/PoseStamped '{ header: {stamp: now, frame_id: \"map\"}, pose: { position: {x: -4.560, y: 0.204, z: 0.0}, orientation: {w: 1.0}}}'"

				cmd = '''rostopic pub -1 /move_base_simple/goal geometry_msgs/PoseStamped "header: 
  seq: 
  stamp: now
  frame_id: "map"
pose: 
  position: 
    x: {x}
    y: {y}
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"'''.format( x=x, y=y)

				

				os.system(cmd)
	except:
		pass



	

	


	
