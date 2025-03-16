import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,500)

polygon = turtle.Turtle()

sides =  6
side_lenght = 70
angle = 360 / sides

for i in range(sides):
    polygon.forward(side_lenght)
    polygon.right(angle)

turtle.done()