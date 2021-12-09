import Tkinter as tk
import os 
import subprocess
import time
import threading
import tf
import rospy
from tf2_msgs.msg import TFMessage

def listener():

	rospy.init_node('listener', anonymous=True)
	a =rospy.wait_for_message("tf", TFMessage)
	return(a)

win = tk.Tk()
win.title("SLAM tutorial")

position_cmd = '''rostopic pub -1 /initialpose geometry_msgs/PoseWithCovarianceStamped  "header: 
  seq: 
  stamp: now
  frame_id: "map"
pose: 
  pose: 
    position: 
      x: 0.731374
      y: -0.044159
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: -0.0395097685597
      w: 0.999219184258
  covariance: [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853892326654787]"'''


point_1 = '''rostopic pub -1 /move_base_simple/goal geometry_msgs/PoseStamped "header: 
  seq: 
  stamp: now
  frame_id: "map"
pose: 
  position: 
    x: -16.8
    y: -22.5
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"'''

point_2 = '''rostopic pub -1 /move_base_simple/goal geometry_msgs/PoseStamped "header: 
  seq: 
  stamp: now
  frame_id: "map"
pose: 
  position: 
    x: -5.6
    y: -0.7
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"'''

point_3 = '''rostopic pub -1 /move_base_simple/goal geometry_msgs/PoseStamped "header: 
  seq: 
  stamp: now
  frame_id: "map"
pose: 
  position: 
    x: 20
    y: -0.85
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"'''

point_4 = '''rostopic pub -1 /move_base_simple/goal geometry_msgs/PoseStamped "header: 
  seq: 
  stamp: now
  frame_id: "map"
pose: 
  position: 
    x: 17.7
    y: -11.3
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"'''

point_5 = '''rostopic pub -1 /move_base_simple/goal geometry_msgs/PoseStamped "header: 
  seq: 
  stamp: now
  frame_id: "map"
pose: 
  position: 
    x: -10
    y: 13.5
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"'''


#functions 
def test_pos(event):
	os.system(position_cmd)
def gazebo_launch():
	os.system("roslaunch husky_gazebo husky_combined.launch")

def stop():
	os.system("pkill roslaunch")

def edit_map():
	os.system("gimp /home/vtl/catkin_ws/src/husky/husky_navigation/maps/map_before_edit.pgm")

def save():
	os.system("rosrun map_server map_saver -f /home/vtl/catkin_ws/src/husky/husky_navigation/maps/map_before_edit")

def navigate_1():
	os.system(point_1)

def navigate_2():
	os.system(point_2)

def navigate_3():
	os.system(point_3)

def navigate_4():
	os.system(point_4)

def navigate_5():
	os.system(point_5)

def navigation_launch():
	os.system("roslaunch husky_navigation amcl_demo.launch")

def good_map_pub():
	os.system("rosrun map_server map_server /home/vtl/catkin_ws/src/husky/husky_navigation/maps/map_after_edit.yaml")

def bad_map_pub():
	os.system("rosrun map_server map_server /home/vtl/catkin_ws/src/husky/husky_navigation/maps/map_before_edit.yaml")

def open_rviz():
	os.system("roslaunch husky_viz nav.launch")

def open_move_base():
	os.system("roslaunch husky_gazebo husky_move_base.launch")

def record_path_cmd():
	os.system("python tf_listener.py")

def use_path_cmd():
	os.system("python path_publish.py")

#def navigation_pose():
#	os.system(position_cmd)

#call back functions

def stop_record(event):
	os.system("pkill -f tf_listener.py")

def record_path(event):
	record_path_thread = threading.Thread(target = record_path_cmd, args=())
	record_path_thread.start()

def use_path(event):
	use_path_thread = threading.Thread(target = use_path_cmd, args=())
	use_path_thread.start()

def move_base(event):
	move_base_demo = threading.Thread(target = open_move_base, args=())
	move_base_demo.start()

def btn_click (event):

	y = threading.Thread(target = gazebo_launch, args=())
	y.start()

def btn_stop(event):
	x = threading.Thread(target = stop(), args=())
	x.start()

def edit_map_btn(event):
	z = threading.Thread(target = edit_map(), args = ())
	z.start()

def save_map(event):
	a = threading.Thread(target = save(), args=())
	a.start()



def navigation(event):
	nav = threading.Thread(target = navigation_launch, args=())
	nav.start()
	os.system(position_cmd)

	
def navigate_btn_1(event):

	n1 = threading.Thread(target = navigate_1, args = ())
	n1.start()


def navigate_btn_2(event):
	
	n2 = threading.Thread(target = navigate_2, args = ())
	n2.start()

def navigate_btn_3(event):
	
	n3 = threading.Thread(target = navigate_3, args = ())
	n3.start()

def navigate_btn_4(event):
	
	n4 = threading.Thread(target = navigate_4, args = ())
	n4.start()

def navigate_btn_5(event):
	
	n5 = threading.Thread(target = navigate_5, args = ())
	n5.start()

def good_map_btn(event):
	gd_map = threading.Thread(target = good_map_pub, args = ())
	gd_map.start()

def bad_map_btn(event):
	bad_map = threading.Thread(target = bad_map_pub, args = ())
	bad_map.start()

def rviz(event):
	rviz_open = threading.Thread(target = open_rviz, args=())
	rviz_open.start()


frame_a = tk.Frame()
frame_b = tk.Frame()

greeting = tk.Label(text="Control panel")
greeting.pack(fill = tk.BOTH, expand = True)

button1 = tk.Button(text = "Start Task 1 SLAM:", width =25, height =5, bg = "#618685", fg = "yellow")
button1.bind("<Button-1>", btn_click)
button1.pack(fill = tk.BOTH, expand = True)

button3 = tk.Button(master = frame_b, text = "Save Map", width =25, height =5, bg = "#80ced6", fg = "yellow")
button3.bind("<Button-1>", save_map)
button3.pack(fill = tk.BOTH, expand = True, side = tk.LEFT)

button4 = tk.Button(master = frame_b, text = "Edit Map", width =25, height =5, bg = "#80ced6", fg = "yellow")
button4.bind("<Button-1>", edit_map_btn)
button4.pack(fill = tk.BOTH, expand = True)

frame_b.pack()

button8 = tk.Button( text = "Start Task2 navigation", width =25, height =5, bg = "#618685", fg = "yellow")
button8.bind("<Button-1>", navigation)
button8.pack(fill = tk.BOTH, expand = True)

#test = tk.Button(text = "Send initial pose", width =25, height =5, bg = "#80ced6", fg = "yellow")
#test.bind("<Button-1>", test_pos)
#test.pack(fill = tk.BOTH, expand = True)


button5 = tk.Button(master = frame_a, text = "Point 1", width =8, height =5, bg = "#80ced6", fg = "yellow")
button5.bind("<Button-1>", navigate_btn_1)
button5.pack(fill=tk.BOTH, side = tk.LEFT)

button6 = tk.Button(master = frame_a, text = "Point 2", width =8, height =5, bg = "#80ced6", fg = "yellow")
button6.bind("<Button-1>", navigate_btn_2)
button6.pack(fill=tk.BOTH, side = tk.LEFT)

button7 = tk.Button(master = frame_a, text = "Point 3", width =8, height =5, bg = "#80ced6", fg = "yellow")
button7.bind("<Button-1>", navigate_btn_3)
button7.pack(fill=tk.BOTH, side = tk.LEFT)


btn_p4 = tk.Button(master = frame_a, text = "Point 4", width =8, height =5, bg = "#80ced6", fg = "yellow")
btn_p4.bind("<Button-1>", navigate_btn_4)
btn_p4.pack(fill=tk.BOTH, side = tk.LEFT)

btn_p5 = tk.Button(master = frame_a, text = "Point 5", width =8, height =5, bg = "#80ced6", fg = "yellow")
btn_p5.bind("<Button-1>", navigate_btn_5)
btn_p5.pack(fill=tk.BOTH, side = tk.LEFT)

frame_a.pack()

frame_d = tk.Frame()
good_map = tk.Button(master = frame_d, text = "Use good map", width =25, height =5, bg = "#80ced6", fg = "yellow")
good_map.bind("<Button-1>", good_map_btn)
good_map.pack(fill=tk.BOTH, side = tk.LEFT)

bad_map = tk.Button(master = frame_d, text = "Use bad map", width =25, height =5, bg = "#80ced6", fg = "yellow")
bad_map.bind("<Button-1>", bad_map_btn)
bad_map.pack(fill=tk.BOTH, side = tk.LEFT)

frame_d.pack()

frame_e = tk.Frame()

move_base_btn = tk.Button(master = frame_e, text = "move base demo", width =25, height =5, bg = "#618685", fg = "yellow")
move_base_btn.bind("<Button-1>", move_base)
move_base_btn.pack(fill = tk.BOTH, side = tk.LEFT)

rviz_btn = tk.Button(master = frame_e, text = "Open RVIZ", width =25, height =5, bg = "#618685", fg = "yellow")
rviz_btn.bind("<Button-1>", rviz)
rviz_btn.pack(fill = tk.BOTH, expand = True)

frame_e.pack()

frame_record = tk.Frame()
record_btn = tk.Button(master = frame_record, text = "record path 1", width =15, height =5, bg = "#618685", fg = "yellow")
record_btn.bind("<Button-1>", record_path)

record_btn.pack(fill = tk.BOTH, side = tk.LEFT)

path_btn = tk.Button(master = frame_record, text = "use path 1", width =15, height =5, bg = "#618685", fg = "yellow")
path_btn.bind("<Button-1>", use_path)
path_btn.pack(fill = tk.BOTH, side = tk.LEFT)

stop_btn = tk.Button(master = frame_record, text = "stop recording", width =15, height =5, bg = "#618685", fg = "yellow")
stop_btn.bind("<Button-1>", stop_record)
stop_btn.pack(fill = tk.BOTH, expand = True)
frame_record.pack()

button2 = tk.Button(text = "quit", width =25, height =5, bg = "red", fg = "yellow")
button2.bind("<Button-1>", btn_stop)
button2.pack(fill = tk.BOTH, expand = True)




win.mainloop()
