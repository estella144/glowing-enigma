import turtle # Import the turtle library  
window = turtle.Screen() # Create a new window  
t = turtle.Turtle() # Create a new turtle called t 
import random # Import random library 

def triangle(x, y):
    t.begin_fill()
    t.penup() 
    t.goto(x,y) 
    t.pendown() 
    for i in range(3): 
        t.forward(20) 
        t.left(120)
    t.end_fill()
    print(f"Drew triangle at x={x}, y={y}")

def square(x, y):
    t.begin_fill()
    t.penup() 
    t.goto(x,y) 
    t.pendown() 
    for i in range(4): 
        t.forward(20) 
        t.left(90)
    t.end_fill()
    print(f"Drew square at x={x}, y={y}")

def rectangle(x, y):
    t.begin_fill()
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(2):
        t.forward(30)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()
    print(f"Drew rectangle at x={x}, y={y}")

def circle(x, y):
    t.begin_fill()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(20)
    t.end_fill()
    print(f"Drew circle at x={x}, y={y}")

again = "y" 
while again != "n":
    again = input("[t]riangle, [s]quare, [r]ectangle, [c]ircle or n to quit: ")
    x = random.randint(-250,250) 
    y = random.randint(-250,250)
    if again == "t":
        triangle(x, y)
    elif again == "s":
        square(x, y)
    elif again == "r":
        rectangle(x, y)
    elif again == "c":
        circle(x, y)
    elif again == "n":
        print("Goodbye")
    else:
        print("Invalid choice! Please try again")
