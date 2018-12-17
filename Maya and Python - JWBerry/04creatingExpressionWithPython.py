#Commented Coding
#JWBerry

#Importing maya commands as cmds to be used later on
import maya.cmds as cmds

cmds.polySphere(r = 5)
#expression -s "pSphere1.rotateY = time * 10;"  -o pSphere1 -ae 1 -uc all ;
cmds.expression(string = 'pSphere1.rotateY = time * 10;',  object = 'pSphere1',ae =True, uc = 'all')
