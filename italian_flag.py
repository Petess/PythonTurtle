import turtle

def setup_screen():
    """Setup the turtle screen"""
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    screen.bgcolor("white")
    screen.title("Italian Flag")
    return screen

def draw_vertical_stripe(t, x_start, stripe_width, flag_height, color):
    """Draw a filled vertical stripe at a specified x_start position"""
    t.penup()
    t.goto(x_start, -flag_height / 2)
    t.pendown()

    t.color(color)
    t.begin_fill()

    # Draw rectangle: go up, right, down, left
    t.setheading(90) # Point up
    t.forward(flag_height)
    t.setheading(0) # Point right
    t.forward(stripe_width)
    t.setheading(270) # Point down
    t.forward(flag_height)
    t.setheading(180) # Point left
    t.forward(stripe_width)

    t.end_fill()


def draw_italian_flag():
    """Draw the Italian flag (Green, White, Red vertical tricolor)"""
    screen = setup_screen()

    # Create drawing turtle
    t = turtle.Turtle()
    t.speed(0) # Fastest speed
    t.hideturtle()
    t.penup()

    # Determine dimensions based on standard ratio (2:3 height:width)
    flag_height = 240
    flag_width = 360 # 240 * (3/2) = 360
    stripe_width = flag_width / 3

    # Position to start drawing the bottom-left corner of the flag
    start_x = -flag_width / 2

    # Draw the stripes first: Green (Left), White (Middle), Red (Right)

    # 1. Green Stripe (Left)
    draw_vertical_stripe(t, start_x, stripe_width, flag_height, "green")

    # 2. White Stripe (Middle)
    # draw_vertical_stripe(t, start_x + stripe_width, stripe_width, flag_height, "white")

    # 3. Red Stripe (Right)
    draw_vertical_stripe(t, start_x + 2 * stripe_width, stripe_width, flag_height, "red")

    # Draw the overall boundary frame *LAST* to ensure it covers all colors
    t.penup()
    t.goto(start_x, -(flag_height/2))
    t.pendown()
    t.color("black")
    t.pensize(2)
    t.setheading(0)
    for _ in range(2):
        t.forward(flag_width)
        t.left(90)
        t.forward(flag_height)
        t.left(90)

    # Keep window open
    screen.mainloop()

if __name__ == "__main__":
    draw_italian_flag()
