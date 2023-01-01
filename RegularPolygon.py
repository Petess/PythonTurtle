from turtle import *

def drawRegularPolygon( sides:int, sidelength:int, filledIn:bool, elColor:str ):
    turnAngle = 360 / sides; 

    color( elColor )
    if filledIn:
        begin_fill()

    for i in range(0,sides):
        forward( sidelength )
        left( turnAngle )

    if filledIn:
        end_fill()


def drawPolygonAt( xLocation:int, yLocation:int, numsides:int, sidelength:int, filledIn:bool, elColor:str ):
    penup()
    home()
    
    forward(xLocation)
    left(90)
    forward(yLocation)
    right(90)
    drawRegularPolygon( numsides, sidelength, filledIn, elColor )

if __name__ == "__main__":
    drawRegularPolygon( 4, 100, True, "red" )
    penup()
    forward(200)
    pendown()
    drawRegularPolygon( 5, 100, False, "blue") 
    penup()
    backward(400)
    pendown()
    drawRegularPolygon( 8,30, True, "green" ) 
    penup()
    right(90)
    forward(150)
    left(90)
    pendown()
    drawRegularPolygon( 3, 100, True, "orange" )

    penup()
    forward(150)

    pendown()

    drawRegularPolygon( 20,10, True, "grey" ) 

    penup()
    forward(150)

    pendown()

    drawRegularPolygon( 20,10, True, "lightgreen" ) 

    drawPolygonAt( 100, 100, 3, 50, True, "green" )

    done()
