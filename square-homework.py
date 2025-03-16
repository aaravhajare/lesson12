import turtle
i = turtle.Screen()
i.bgcolor("aqua")
i.setup(400,400)
i.title("square")

pen = turtle.Turtle()

side = 4
s_lenght = 50
angle = 90

for a in range(side):
    pen.forward(s_lenght)
    pen.right(angle)

turtle.done()