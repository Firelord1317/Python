import turtle   
my_wn = turtle.Screen()
my_wn.bgcolor("lightgreen")
my_wn.title("Spiral Pattern")
my_pen = turtle.Turtle()
size = 5
while True:
    for i in range(4):
        my_pen.fd(size + 1)
        my_pen.left(90)
        size += 3
    size += 1

