import turtle

window = turtle.Screen()
window.title("PISB Python SIG")

t1 = turtle.Turtle()
t1.fillcolor("blue")

for i in range(6):
    for _ in range(3):
        t1.forward(200)
        t1.left(120)
    t1.left(60)

    if i%2 == 0:
        t1.begin_fill()
    else:
        t1.end_fill()

t1.penup()
turtle.done()