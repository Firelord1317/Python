import turtle
loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
    turtle.circle(5*1)
    turtle.circle(-5*1)
    turtle.left(i)
turtle.exitonclick()