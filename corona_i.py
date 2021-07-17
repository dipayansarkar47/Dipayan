import turtle
a=0
b=0
turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("green")
turtle.penup()
turtle.goto(0,200)
turtle.pendown()

while True:
    turtle.forward(a)
    turtle.right(b)
    a+=3
    b+=1
    if b==201:
        break
turtle.done()
