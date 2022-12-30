import turtle
import tkinter as TK

def squareAt( elt:turtle, squareSize, x, y, col ):
    elt.penup()
    elt.home()
    
    elt.forward(x)
    elt.left(90)
    elt.forward(y)

    elt.color( col )
    elt.pendown()

    elt.forward(squareSize)
    elt.right(90)
    elt.forward(squareSize)
    elt.right(90)
    elt.forward(squareSize)
    elt.right(90)
    elt.forward(squareSize)
    elt.right(90)

print("hello")

t = turtle.Turtle()

squareAt( t, 50, -20, -30, 'red' )
squareAt( t, 100, 40, 40, 'green' )
squareAt( t, 100, 0, 0, 'blue' )
squareAt( t, 100, 200, 200, 'yellow'  )

TK.mainloop()


