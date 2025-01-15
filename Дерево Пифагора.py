import turtle

def draw_pythagoras_tree(x, y, size, angle, depth):
    if depth == 0:
        return

    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angle)
    turtle.pendown()

    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size * (2 ** 0.5))
    turtle.left(90)
    turtle.forward(size * (2 ** 0.5))
    turtle.left(45)

    new_size = size * 0.7


    draw_pythagoras_tree(x + new_size, y + new_size, new_size, angle - 45, depth - 1)


    draw_pythagoras_tree(x + new_size, y + new_size, new_size, angle + 45, depth - 1)


turtle.speed(0)
turtle.bgcolor("white")

# Начальные параметры
initial_size = 100  # Размер основания дерева
initial_angle = 90  # Угол наклона
initial_depth = 7   # Глубина рекурсии

# Рисуем дерево Пифагора
draw_pythagoras_tree(-50, -150, initial_size, initial_angle, initial_depth)

# Завершаем рисование
turtle.done()