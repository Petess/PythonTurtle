from numbers import Number
import turtle
import random

t = turtle.Turtle()
t.speed(0)



def drawCube( xLocation:float, yLocation:float, size:float, skewAngle:float, 
    shortening:float ):
    t.penup()
    t.home()
    t.goto(xLocation,yLocation)
    t.pendown()

    # draw a square 
    for i in range(4): 
        t.forward(size)
        t.left(90)

    t.forward(size)
    t.left(skewAngle)
    t.forward( size / shortening )
    t.left( 90 - skewAngle )
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(skewAngle)
    t.forward( size / shortening )
    t.left( 90 + skewAngle )
    t.forward( size )
    t.left(skewAngle)
    t.forward( size / shortening )
    
    
    return

def drawRandomCubes( numToDraw:int):
    for i in range( numToDraw ):
        xRandLocation = random.randint( -200, 200)
        yRandLocation = random.randint( -200, 200)
        cubeSize = random.randint( 10, 100 )
        drawCube( xRandLocation, yRandLocation, cubeSize, 45, 2) 

drawRandomCubes( 7 ) 

turtle.done()