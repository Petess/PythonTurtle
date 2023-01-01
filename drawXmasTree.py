from turtle import *

from RegularPolygon import drawPolygonAt, drawRegularPolygon


if __name__ == "__main__":
    
    xLoc = 0
    yLoc = 0
    size = 150
    sizeDecrement = 10
    yIncrement = 30

    for i in range(6):
        drawPolygonAt( xLoc, yLoc, 3, size, True, "green" )
        yLoc = yLoc + yIncrement
        size = size - sizeDecrement
        xLoc = xLoc + ( sizeDecrement / 2 ) 

    done()