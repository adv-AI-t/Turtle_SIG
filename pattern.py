import turtle

t1 = turtle.Turtle()

for _ in range(6):
    for _ in range(6):
        t1.forward(50)
        t1.left(60)
    t1.forward(10)

t1.penup()
turtle.done()
