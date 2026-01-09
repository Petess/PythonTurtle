import turtle

def setup_screen():
    """Setup the turtle screen with white background"""
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    screen.bgcolor("white")
    screen.title("Japanese Flag (Hinomaru)")
    return screen

def draw_circle(t, radius, color):
    """Draw a filled circle"""
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_japanese_flag():
    """Draw the Japanese flag (White field with a large red disc in the center)"""
    screen = setup_screen()

    # Create drawing turtle
    t = turtle.Turtle()
    t.speed(0) # Fastest speed
    t.hideturtle()
    t.penup()

    # Dimensions based on standard ratio (2:3 height:width)
    flag_height = 240
    flag_width = 360

    # The disc diameter is 3/5 of the height.
    disc_radius = int((3/5 * flag_height) / 2)

    # 1. Draw the Red Disc (Hinomaru) - Centered at (0, 0)
    t.home() # Reset orientation and move to (0, 0)
    t.goto(0, -disc_radius)
    t.pendown()
    draw_circle(t, disc_radius, "red")

    # 2. Draw the White Field Boundary (Outline)
    t.penup()
    # Move to bottom-left corner for boundary drawing
    start_x = -flag_width / 2
    start_y = -flag_height / 2
    t.goto(start_x, start_y)
    t.pendown()

    t.color("black")
    t.pensize(2)
    for _ in range(2):
        t.forward(flag_width)
        t.left(90)
        t.forward(flag_height)
        t.left(90)

    # Keep window open
    screen.mainloop()

if __name__ == "__main__":
    draw_japanese_flag()
