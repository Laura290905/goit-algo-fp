import turtle
import math

def draw_tree(depth, size):
    if depth == 0:
        turtle.forward(size)
        turtle.backward(size)
        return

    # Draw the main trunk
    turtle.forward(size)

    # Draw the left branch
    turtle.left(45)
    draw_tree(depth - 1, size * math.sqrt(2) / 2)
    turtle.right(45)

    # Draw the right branch
    turtle.right(45)
    draw_tree(depth - 1, size * math.sqrt(2) / 2)
    turtle.left(45)

    # Return to the original position
    turtle.backward(size)

# Initial turtle setup
turtle.speed('fastest')
turtle.left(90)  # Pointing the turtle upward
turtle.color("green")

# Draw the Pythagorean tree
draw_tree(5, 100)  # Example: depth 5, size 100

# Finish the drawing
turtle.done()