#Commented Coding
#JWBerry

#Importing maya commands as cmds to be used later on
import maya.cmds as cmds
#Importing math to use Sin in my rotation
import math

for i in range (1, 73):
    #creating the sphere
    cmds.sphere()
    
    #Then I move the sphere off from the center
    cmds.move(0, 0, -10, relative = True) #relative is okay here becuase I know the sphere is starting from 0,0,0, so it's the same as absolute
    
    #now to move the pivot point towards the center, making sure to increment the nurbsSphere thingy by one everytime by inserting ' + str(i) + '
    cmds.move(0, 0, 10, ('nurbsSphere' + str(i) + '.scalePivot'), ('nurbsSphere' + str(i) + '.rotatePivot'))
    
    #now to rotate the spheres
    cmds.rotate(0, i*5, 0, r =True, os = True)
    
    #now I'm using sin to assign a new y position
    yTranslate = math.sin(math.radians(5 * i))
    
    cmds.move(0, yTranslate, 0, r = True)
    
