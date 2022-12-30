from turtle import *


def lineToCircle( angle:int, circleRadius:int, lineLength:int, elColor:str ):
    color( elColor )
    left(angle)
    forward( lineLength )
    circle( circleRadius ) 
    home()


# lineToCircle( 10, 20, 100, "green" )

speed()
segments = 20

angleForSegment = 360 / segments

colorList = [ "red", "green", "blue", "pink", "lightblue", "purple" ]

lineLength = 30
lineLengthIncrement = 10

for i in range(0,segments):
    lineToCircle( i * angleForSegment, 20, lineLength, colorList[ i % len(colorList) ] )
    lineLength = lineLength + lineLengthIncrement 

done()


