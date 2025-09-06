import turtle
turtle.Screen().bgcolor("Aqua")
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
turtle.setx(0)
turtle.sety(0)
my_pen = turtle.Pen()
turtle.bgcolor("black")

for i in range(5):
    my_pen.forward(200)
    my_pen.right(90)
    my_pen.pencolor(colors[i % 4])

turtle.done()