import Tkinter as tk
import os 
import subprocess
import time

win = tk.Tk()
win.title("SLAM tutorial")

def quit_ros (event):
	os.system("pkill roslaunch")

greeting = tk.Label(text="Hello, Tkinter")
greeting.pack(fill = tk.BOTH, expand = True)

button1 = tk.Button(text = "Task 1", width =25, height =5, bg = "blue", fg = "yellow")
button1.bind("<Button-1>", quit_ros)
button1.pack(fill = tk.BOTH, expand = True)


win.mainloop()
