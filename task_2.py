import turtle

def draw_pifagoras_tree(branch_length, t, angle, level):
    if level == 0:
        return
    else:
        t.forward(branch_length)
        t.right(angle)

        draw_pifagoras_tree(0.7 * branch_length, t, angle, level - 1)

        t.left(2 * angle)

        draw_pifagoras_tree(0.7 * branch_length, t, angle, level - 1)

        t.right(angle)
        t.backward(branch_length)

def main():
    recursion_level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(2)

    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    draw_pifagoras_tree(100, t, 30, recursion_level)

    screen.exitonclick()

if __name__ == "__main__":
    main()
