#!/usr/local/bin/python3


# Code starts running following this.
# If this file is use as "import local" then the stuff below doesn't run and isn't available.
print (""" test of imports """)
import sys
import math
import turtle
import tkinter

""" A nice little window to add to a developing project
    to add a handy exit  to it if tkinter is already being used.
    otherwise copy and paste the lines below this for a
    stand alone window    
"""
def EndIt():
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH,expand=1)
    button = tkinter.Button(frame,text="Exit",command=tk.destroy)
    button.pack(side=BOTTOM)
  

if __name__ == "__main__":
# local functions and global data is set up here before the if __name__ == "__main__":
	
    print ("python3.5  successfully imported sys, math, turtle, and tkinter")
    
    from tkinter.constants import *
    tk = tkinter.Tk()
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH,expand=1)
    label = tkinter.Label(frame, text=" python3 successfully imported \n sys, math, turtle, and tkinter ")
    label.pack(fill=X, expand=1)
    button = tkinter.Button(frame,text="Exit",command=tk.destroy)
    button.pack(side=BOTTOM)
    tk.mainloop()