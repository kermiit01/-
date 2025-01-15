import turtle

def draw_square(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
def draw_t_square(x, y, size, depth):
    if depth == 0:
        return
    draw_square(x, y, size)
    new_size = size / 3
    draw_t_square(x - new_size, y - new_size, new_size, depth - 1)
    draw_t_square(x + new_size, y - new_size, new_size, depth - 1)
    draw_t_square(x - new_size, y + new_size, new_size, depth - 1)
    draw_t_square(x + new_size, y + new_size, new_size, depth - 1)
    draw_t_square(x, y, new_size, depth - 1)

turtle.speed(0)
turtle.bgcolor("white")


initial_size = 300
initial_depth = 4


draw_t_square(0, 0, initial_size, initial_depth)


turtle.done()