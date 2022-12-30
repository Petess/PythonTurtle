from turtle import *

colors = [ "red", "green", "blue", "orange"]
square_side = 90

for i in range(1,5):
    for elcolor in colors:
        color( elcolor )
        for side in range(1,4):
            forward( square_side )
            left(90)
        left(5)

done()
