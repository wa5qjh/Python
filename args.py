# args.py - command line argument processing

# dalem@QnD:~/PycharmProjects/Python⟫ python3 args.py test
# ['args.py', 'test']


import sys

print (sys.argv)

print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))

#
