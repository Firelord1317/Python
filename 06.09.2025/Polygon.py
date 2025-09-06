import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(800, 600)
polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()