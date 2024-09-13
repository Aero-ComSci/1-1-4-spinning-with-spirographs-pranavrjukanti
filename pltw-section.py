import turtle as trtl #Importing Turtle
painter = trtl.Turtle()

painter.penup()
painter.goto(-719,-35.5)
painter.pendown()


painter.left(45)
painter.forward(50)

g=0
p=0

x=True
while x:

    painter.right(90)
    painter.forward(50)
    painter.left(90)
    painter.forward(50)
    g=g+0.5
    p=p+0.5
    if g==10:
        painter.penup()
        painter.goto(-719,-35.5)
        painter.pendown()
    if p==21:
        break









wn = trtl.Screen()
wn.mainloop()
