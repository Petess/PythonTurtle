import turtle

def draw_rectangle(t, width, height, color):
    """Draws a filled rectangle."""
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_belgian_flag():
    """Draws the Belgian flag using the turtle graphics module."""
    screen = turtle.Screen()
    screen.setup(width=800, height=550)
    screen.title("Belgian Flag")
    
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.hideturtle()
    
    # Flag dimensions (approximate ratio 13:10)
    flag_width = 650
    flag_height = 500
    
    # Calculate the width of each vertical stripe
    stripe_width = flag_width / 3.0
    
    # Move to the starting position (bottom-left corner)
    t.penup()
    t.goto(-flag_width / 2, flag_height / 2)
    t.pendown()
    
    # Define colors (Black, Yellow, Red)
    colors = ["black", "gold", "red"]
    
    # Draw the three vertical stripes
    for i in range(3):
        # Set color for the current stripe
        t.fillcolor(colors[i])
        t.pencolor(colors[i])
        
        t.begin_fill()
        for _ in range(2):
            t.forward(stripe_width)
            t.right(90)
            t.forward(flag_height)
            t.right(90)
        t.end_fill()
        
        # Move to the start of the next stripe
        t.forward(stripe_width)
        
    # Keep the window open until manually closed
    screen.mainloop()

if __name__ == "__main__":
    draw_belgian_flag()