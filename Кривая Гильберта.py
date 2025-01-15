import turtle


def levi_curve(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        levi_curve(length / 2, depth - 1)
        turtle.left(45)
        levi_curve(length / 2, depth - 1)
        turtle.right(90)
        levi_curve(length / 2, depth - 1)
        turtle.left(45)
        levi_curve(length / 2, depth - 1)


turtle.speed(0)
turtle.bgcolor("white")


initial_length = 300
depth = 6


turtle.penup()
turtle.goto(-initial_length / 2, 0)
turtle.pendown()


levi_curve(initial_length, depth)


turtle.done()