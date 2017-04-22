#!/usr/local/bin/python3

# local functions and global data is set up here before the if __name__ == "__main__":

# Code starts running following this.
# If this file is use as "import local" then the stuff below doesn't run and isn't available.
if __name__ == "__main__":

    print (""" test of imports """)
    import sys
    import math
    import turtle
    import tkinter

    print ("python3.5  successfully imported sys, math, turtle, and tkinter")

    from tkinter.constants import *
    tk = tkinter.Tk()
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH,expand=1)
    label = tkinter.Label(frame, text="  My local.py so far! \n ")
    label.pack(fill=X, expand=1)
    button = tkinter.Button(frame,text="Exit",command=tk.destroy)
    button.pack(side=BOTTOM)
    tk.mainloop()

