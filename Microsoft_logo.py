# draw color-filled square in turtle

import turtle

# creating turtle pen
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
# taking input for the side of the square
s = 100

# taking the input for the color
col = "red"
t.penup()
t.goto(-100,100)
t.pendown()
# set the fillcolor
t.fillcolor(col)

# start the filling color
t.begin_fill()

# drawing the square of side s
for _ in range(4):
    t.forward(s)
    t.right(90)

# ending the filling of the color
t.end_fill()


col = "#42fc77"
t.penup()
t.goto(5,100)
t.pendown()
# set the fillcolor
t.fillcolor(col)

# start the filling color
t.begin_fill()

# drawing the square of side s
for _ in range(4):
    t.forward(s)
    t.right(90)

# ending the filling of the color
t.end_fill()


col = "#0091ff"
t.penup()
t.goto(-100,-5)
t.pendown()
# set the fillcolor
t.fillcolor(col)

# start the filling color
t.begin_fill()

# drawing the square of side s
for _ in range(4):
    t.forward(s)
    t.right(90)

# ending the filling of the color
t.end_fill()


col = "yellow"
t.penup()
t.goto(5,-5)
t.pendown()
# set the fillcolor
t.fillcolor(col)

# start the filling color
t.begin_fill()

# drawing the square of side s
for _ in range(4):
    t.forward(s)
    t.right(90)

# ending the filling of the color
t.end_fill()
t.penup()
t.goto(-225,-200)
t.pendown()
t.color("white")
t.write("Microsoft Logo by @codewithbiki", font=("Arial", 20, "normal"))

turtle.done()