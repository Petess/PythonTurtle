import turtle

def setup_screen():
    """Setup the turtle screen"""
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    screen.bgcolor("white")
    screen.title("German Flag")
    return screen

def draw_rectangle(t, width, height, color):
    """Draw a filled rectangle"""
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_german_flag():
    """Draw the German flag (Black, Red, Gold horizontal tricolor)"""
    screen = setup_screen()
    
    # Create drawing turtle
    t = turtle.Turtle()
    t.speed(0) # Fastest speed
    t.hideturtle()
    t.penup()
    
    # Determine dimensions based on standard ratio (3:5)
    flag_width = 300
    flag_height = 180 # 300 * (3/5) = 180
    stripe_height = flag_height / 3
    
    # Position to start drawing the bottom-left corner of the flag
    start_x = -flag_width / 2
    start_y = -flag_height / 2
    
    # Drawing order: Bottom (Gold), Middle (Red), Top (Black)

    # 1. Gold Stripe (Bottom)
    t.goto(start_x, start_y)
    t.pendown()
    draw_rectangle(t, flag_width, stripe_height, "gold")
    
    # 2. Red Stripe (Middle)
    t.penup()
    t.goto(start_x, start_y + stripe_height)
    t.pendown()
    draw_rectangle(t, flag_width, stripe_height, "red")
    
    # 3. Black Stripe (Top)
    t.penup()
    t.goto(start_x, start_y + 2 * stripe_height)
    t.pendown()
    draw_rectangle(t, flag_width, stripe_height, "black")
    
    # Keep window open
    screen.mainloop()

if __name__ == "__main__":
    draw_german_flag()