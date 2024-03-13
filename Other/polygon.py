from turtle import Turtle

t = Turtle()
t.speed(0)

while True:
    sides = int(input("Number of sides: "))
    side_length = float(input("Side length (pixels): "))
    colour = input("Colour: ").lower()
    fill = input("Fill? [Y/N] ").lower()

    internal_angle = 360 / sides
    t.color(colour)

    if fill == 'y':
        t.begin_fill()

    for i in range(0, sides):
        
        t.pd()
        t.forward(side_length)
        t.left(internal_angle)
    
    t.end_fill()
        
