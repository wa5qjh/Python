#!/usr/local/bin/python3


# Code starts running following this.
# If this file is use as "import local" then the stuff below doesn't run and isn't available.
print (""" test of imports """)
import sys
import math
import turtle
import tkinter

# Frequently used
# constants, weights and measures
Km2mi =0.6214	# lilometer to miles
in2mm =  25.4		#inches to millimeters
y2m = .9144		# yards to meters
pi=3.14159256
# e= 2.7182818284590452353602874713526624977572470936999
Naperian = 2.718281828459  #trimmed to a reasonable precision
C = 299 			# Speed of light in  meters/s
#  quick conversions

def FtoC(tempF) :
	return (tempF - 32)* 0.5555555
    
def CtoF(tempC):
	return (tempC *1.8)  +32




#     #### 	 tkinter 		######
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

# my conversions
    print ( "  85 Deg-F to Deg-C  is %.1f " % FtoC(85))
    print ( "  25 Deg-C to Deg-F  is %.1f \n" %  CtoF(25))



    from tkinter.constants import *
    tk = tkinter.Tk()
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH,expand=1)
    label = tkinter.Label(frame, text=" python3 successfully imported \n sys, math, turtle, and tkinter ")
    label.pack(fill=X, expand=1)      # lets add a few more labels
    label2 = tkinter.Label( frame, text = ( " 75F to C conversion %.1f" % FtoC(75)  )  )
    label3 = tkinter.Label( frame, text = ( " 25C to F conversion %.1f \n" % CtoF(25)  )  )
    label2.pack(fill=X, expand=1)
    label3.pack(fill=X, expand=1)
    # then  "Gitt outa Dodge!"
    button = tkinter.Button(frame,text="Exit",command=tk.destroy)
    button.pack(side=BOTTOM)
    tk.mainloop()


