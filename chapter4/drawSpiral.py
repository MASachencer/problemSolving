import turtle


def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 1)


my_turtle = turtle.Turtle()
my_win = turtle.Screen()
draw_spiral(my_turtle, 200)
my_win.exitonclick()
