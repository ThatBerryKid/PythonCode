#Maya and Python Plus Berry
#This is JW.Berry's quick guide for beginner to intermediate Maya users
#who are interested in learning Python's use in Maya. This Code has examples
#taken from an online tutorial explaining coding in Maya in more complicated
#terms. JW.Berry hopes this is more simplfied. Running this code as is will
#create a bunch of nurbs spheres and poly cubes used in the examples below.
#To learn it step by step, comment out example code you are not currently testing.




##First -- Translation##
#Learning how to convert MEL commands into Python
#JW.Berry
#First, you should import maya.cmds and place it as cmds
import maya.cmds as cmds

#Example 1, writing commands
#To create a simple sphere, you can use the MEL "sphere;" code.
#Translating into Python, you must add "cmds."
#and call the sphere function => "cmds.sphere()"
cmds.sphere()

#Example 2, more translation
#MEL uses dashes infront of it's flags like "sphere -r 10;" for a sphere
#to be generated with a radius of 10. In python, the change is that you put
#the flag into the function's arguements and remove the dash,
#"cmds.sphere( r = 10 )
cmds.sphere( r = 10 )

#Example 3, using first irregular translation
#Moving in maya MEL is "move -r float float float " the move command with
#a relative (r) or absolute (a) flag and then a three dimensonal coordinate
#or where to move it. In Python, the "-r" flag turns into "r" but goes at the
#end of the arguments, which are now separated by commas.
cmds.move(0, 10, 0, r = True);



##Second -- Variables##
#JW.Berry
#Example 1, declaring variables
#In MEL 'int', 'float', 'string', 'list', and other types exist for
#variables. In python, you do not need to identify the 'int', 'float', etc.
myInt = 5
myFloat = 5.6
myString = 'JW.Berry'
myList = []

#Example 2, operations with variables
#You can do the order of operations on the variable types
#like you would normally. Just make sure you remember what
#types are automatically assigned to your variables
newInt = myInt/2
print newInt #This would print out '2', because "5 / 2" would equal '2.5' but since
#myInt is an integer it cuts off the decimal number completely regardless
#of if it should be rounded up or down.
#operations work on strings as well
newString = ' is an awesome animator!'
print(myString + newString) #This would ouput 'JW.Berry is an awesome animator!'
#Strings and ints can not operate on each other without a conversion.
#Converting an int:
print(myString + str(myInt)) #This would output 'JW.Berry5', because of the added
#'str( )' that changed myInt from 5 the number, into "5" the text character.


##Third == For Loops##
#JW.Berry
#Example 1, for loop syntax
#A python for loop is made the same way in maya as it is out of maya.
#It looks like this ' for i in range(0,10): ' with 'i' being any name for something
#that will be increased by one in the loop until it reaches the end of the set range.
#In python, you must always indent when you write the code that will be looped inside the code. 

for i in range(0,10): #This can also just be range(10).

    cmds.polyCube() #the for loop function will create a polyCube (Learned that from creating a polyCube from the UI and then translating the MEL into python

    cmds.move(0,i,0) #then it will move the polyCube it is currently selecting on upwards by the variable that increments by one every time.


#Note from James: At this point, if you know how to code in Java for Processing, then you know enough
#right now to be able to create some cool 3D scenes with programmed duplication. Verrry cool skill to know.

#Example 2, looping and moving
for i in range(20):
    cmds.sphere()
    cmds.move(i*2,0,0) #This will create a line of spheres that are each 2 units away
    #from the previous one, on the X axis.


#Example 3, nested for loop 2D
for i in range(20):
    for j in range(20):
        cmds.sphere()
        cmds.move(i*2,15,j*2) #This will cycle through both for loops AT 15 ON THE Y Axis, I moved it in case the
        #scene was getting too messy.
#'j' is like 'i' as I said before, they are just variables for the incremented value
#That took me a long time to figure out. So I could have named them for JWB in range(20)

#Example 3.2, going into the 3rd dimension!
#Let's make the for loop create a 10x10x10 matrix of spheres!
for i in range(10):
    for j in range(10):
        for JWB in range(10):
            cmds.sphere()
            cmds.move(i*3,JWB*3,j*3) #That's so coool!!!! Comment out the other code and just admire this output
            #Really, that's hecka cool! We basically made the X axis increment 10 times and the same for the Y axis and Z axis. Creating a matrix, or cube!

farewellMessage= 'Well, this is where I say goodbye for the beginner to intermediate level python quick quide. I want to start making cool 3D scenes from these examples already!'
print(farewellMessage)