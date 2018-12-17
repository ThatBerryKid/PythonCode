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
    cmds.move(0, 0, -5, relative = True) #relative is okay here becuase I know the sphere is starting from 0,0,0, so it's the same as absolute
    
    #now to move the pivot point towards the center, making sure to increment the nurbsSphere thingy by one everytime by inserting ' + str(i) + '
    cmds.move(0, 0, 5, ('nurbsSphere' + str(i) + '.scalePivot'), ('nurbsSphere' + str(i) + '.rotatePivot'))
    
    #now to rotate the spheres
    cmds.rotate(0, i*5, 0, r =True, os = True)
    
    #now I'm using sin to assign a new y position
    yTranslate = math.sin(math.radians(5 * i))
    
    #and moving them again
    cmds.move(0, yTranslate, 0, r = True)
    
    ##Now I copy and pasted my expression example in here to make them all move around in a wavy motion
    cmds.expression(string = 'nurbsSphere' + str(i) + '.translateY = sin(time + ' + str(i) +');', object = 'nurbsSphere' + str(i), ae = True, uc = 'all')

#cmds.polySphere(r=5)
###expression -s "pSphere1.rotateY = time * 10;"  -o pSphere1 -ae 1 -uc all ;
#cmds.expression(string = 'pSphere1.rotateY = time * 10;',  object = 'pSphere1',ae =True, uc = 'all') ;

