#Commented coding
#JW.Berry

#Importing Maya Commands as cmds
import maya.cmds as cmds

#Making a 2D vertical grid of polySpheres
for j in range(20):
    for i in range(20):
        cmds.polySphere( name = "James " + str(i))
        cmds.move( 0, i, j, r = True)
        
#Using Python's "ls" command for list creation with the flag, " selection = true ", I will get returned a list with currently selected
#shapes
sel = cmds.ls(selection = True)
print sel

#printing the Length of the list with "len" command
length = len(sel)
print length

#adding on to the list
sel.append('JamesBerry')

#Python lists are 0-indexed, so above append is
print sel[length-1]