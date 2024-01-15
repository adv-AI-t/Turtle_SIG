import turtle

window = turtle.Screen()
window.title("PISB Python SIG")

t1 = turtle.Turtle()

#draw triangle using loops
t1.fillcolor("blue")    #specify color of the turtle
t1.begin_fill()         #start filling
for _ in range(6):
    t1.forward(150)
    t1.left(60)
t1.end_fill()           #end filling
#draw hexagon using loops

# for _ in range(6):
#     t1.forward(100)
#     t1.left(60)
# t1.left(30)

t1.penup()
turtle.done()