import turtle
t = turtle.Turtle()

def talloval(r):
    turtle.left(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)

talloval(100)
