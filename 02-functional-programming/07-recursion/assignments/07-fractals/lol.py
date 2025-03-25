import turtle  # Assuming turtle graphics

def recursive_draw(tur, x, y, length, angle, count):
    if count <= 0:
        return  # Stop recursion when count reaches 0
    
    # Move to starting position
    tur.penup()
    tur.goto(x, y)
    tur.setheading(angle)  # Set initial angle (e.g., 90 for upward)
    tur.pendown()
    
    # Draw the trunk
    tur.forward(length)
    
    # Get new position after drawing trunk
    new_x, new_y = tur.xcor(), tur.ycor()
    
    # Draw left branch
    tur.left(45)  # Turn 45 degrees left
    tur.forward(length * 0.7)  # Shorter branch
    recursive_draw(tur, tur.xcor(), tur.ycor(), length * 0.7, tur.heading(), count - 1)
    tur.backward(length * 0.7)  # Return to split point
    
    # Draw right branch
    tur.right(90)  # Turn 90 degrees right (45 from original angle)
    tur.forward(length * 0.7)  # Shorter branch
    recursive_draw(tur, tur.xcor(), tur.ycor(), length * 0.7, tur.heading(), count - 1)
    tur.backward(length * 0.7)  # Return to split point

# Example usage
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
recursive_draw(t, 0, -200, 100, 90, 3)  # Start at (0, -200), length 100, angle 90°, 3 levels
turtle.done()