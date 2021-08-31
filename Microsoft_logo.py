import turtle


t = turtle.Turtle()
turtle.Screen().bgcolor("black")
s = 100
col = "red"
t.penup()
t.goto(-100,100)
t.pendown()
t.fillcolor(col)
t.begin_fill()

for _ in range(4):
    t.forward(s)
    t.right(90)
t.end_fill()


col = "#42fc77"
t.penup()
t.goto(5,100)
t.pendown()
t.fillcolor(col)


t.begin_fill()

for _ in range(4):
    t.forward(s)
    t.right(90)
t.end_fill()


col = "#0091ff"
t.penup()
t.goto(-100,-5)
t.pendown()
# set the fillcolor
t.fillcolor(col)

t.begin_fill()

for _ in range(4):
    t.forward(s)
    t.right(90)

t.end_fill()


col = "yellow"
t.penup()
t.goto(5,-5)
t.pendown()
# set the fillcolor
t.fillcolor(col)

t.begin_fill()
for _ in range(4):
    t.forward(s)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-225,-200)
t.pendown()
t.color("white")
t.write("Microsoft Logo by @codewithbiki", font=("Arial", 20, "normal"))

turtle.done()
