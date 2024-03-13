import turtle
tina = turtle.Turtle()
tina.shape("turtle")

colours = ["#ff0000",
           "#ffc450",
           "#b6ff24",
           "#00ff00",
           "#24ffb6",
           "#10afff",
           "#1c1cff",
           "#aa00ff",
           "#ff0cae",
           "#ff0000"]

for i in range(1, 11):
  c = colours[i-1]
  tina.color(c)
  tina.circle(i*10)
  print("Drew circle with size", i*10, "and colour", c)
  tina.right(90)
  tina.pu()
  tina.forward(10)
  tina.left(90)
  tina.pd()
