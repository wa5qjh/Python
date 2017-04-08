#!/usr/local/bin/python3
import math
import sys

print (math)
print (sys)
"""
sqare root function
 y = (x + a/x)/2

"""

def sqrt( a ) :
    y=1.0			# force floating point
    x=a
    while x != y :
        x=y        
        y = ( x + a/x ) / 2
    return y

#    ----------    
print ( "\n\t Testing my sqrt vs math.sqrt \n")
tri=556
print (sys.version_info)
if sys.version_info[ 0] ==  3 :
    print ("\t\t py3 My sqrt of %d is %.5f " %  (tri, sqrt( tri ) ) )
    print ("\t\t math.sqrt \t %.5f" % math.sqrt( tri ) )
else:
    print ("\t\t py2 My sqrt of %d is  %.5f " %  ( tri, sqrt( tri ) ) )
    print ("\t\t math.sqrt \t %.5f" %  math.sqrt( tri ) )
    

