#Commented Code
#JW.Berry


#I import my maya commands as commands, and I import random to be used on my instances
import maya.cmds as cmds
import random
#NOW TO GET FANCY I IMPORT MATH
import math


#I set a random seed, which is a unique random list that doesn't change after being created, changing the number changes which random list I get
random.seed ( 1234 )

result = cmds.ls (orderedSelection = True)


''' this code was to delete previous cubes when running new code
if len( cubeList ) > 0:
    cmds.delete( cubeList )
''' 
#I declared an instance to be the transform of the cube shape. They consist of two objects, the
#transform and the shape. So I set it to result[0] to get the transform item
nameForInstance = result[0]

#I group the objects (this was done afterwards)
instanceGroupName = cmds.group (empty = True, name = nameForInstance + 'instance_group#' )



#I start my for loop
for i in range (1,50):
    #I create a new instance
    instanceResult = cmds.instance( nameForInstance, name = nameForInstance)
    cmds.parent( instanceResult, instanceGroupName) #JUST LIKE PRESSING CONTROL P, This parents the first object to the second one!
    #I randomize my values for the x,y,z coordinates using the import random command earlier.
    x = random.uniform(-20, 20)
    y = random.uniform(0, 40)
    z = random.uniform(-20, 20)  
    #then I move each instance to random locations using the random numbers.  
    cmds.move (x,y,z, instanceResult)
    #next I do the same for the rotation values
    xRotate = random.uniform(0,360)
    yRotate = random.uniform(0,360)
    zRotate = random.uniform(0,360)
    #Then, I apply the values in a rotate command
    cmds.rotate( x, y, z, instanceResult)
    #I create my changing up and down variable with Sine
    upAndDown = math.sin ( math.radians(i * 5 ))
    #I initially move them with the variable
    cmds.move (0, upAndDown, 0, instanceResult, relative =True)
    #Then I animate them with that expression!
    cmds.expression(string = 'strawB' + str(i) +'.translateY = sin(time+' +str(i) + ');', object = 'strawB' +str(i), ae=True, uc='all')
    
    
cmds.hide( nameForInstance )
cmds.xform( instanceGroupName, centerPivots = True)
    