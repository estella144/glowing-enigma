import turtle
tina = turtle.Turtle()

def move(turtle, pos_x, pos_y):
    turtle.pu()
    turtle.goto(pos_x, pos_y)
    turtle.pd()

def triangle(color, side_length, fill):
    tina.color(color)
    print(f"Set turtle color to {color}")
    if fill:
        print("Began fill")
        tina.begin_fill()
    for i in range(3):
        tina.right(120)
        tina.forward(side_length)
        print(f"Drew side: length {side_length} angle 120")
    tina.end_fill()

def square(color, side_length, fill):
    tina.color(color)
    print(f"Set turtle color to {color}")
    if fill:
        tina.begin_fill()
        print("Began fill")
    for i in range(4):
        tina.right(90)
        tina.forward(side_length)
        print(f"Drew side: length {side_length} angle 90")
    tina.end_fill()

square("black", 100, True)
tina.right(180)
tina.forward(100)
triangle("black", 100, True)
