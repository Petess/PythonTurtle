from numbers import Number
import turtle
import random

t = turtle.Turtle()
t.speed(0)

def drawLineCurve( xHeight:float, yHeight:float, xDivisions:int,
                   yDivisions:int ):
   
    xDivisionSize = xHeight / xDivisions
    yDivisionSize = yHeight / yDivisions
        
    x = 0;
    y = yHeight;
 
    while( x <= xHeight ):
        t.penup()
        t.home()
        t.goto( x, 0 )
        t.pendown()
        t.goto( 0, y )

        x = x + xDivisionSize
        y = y - yDivisionSize       
        
    return


drawLineCurve( 500, 500, 10, 10 )


turtle.done()