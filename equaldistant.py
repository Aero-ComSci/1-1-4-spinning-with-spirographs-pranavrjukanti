
#Question
print("How many sqaure do you want?")
s=int(input())




import turtle as trtl #Importing Turtle
painter = trtl.Turtle()
screen = trtl.Screen()
screen.setup(width=800, height=800)

if s==2:

    #math
    rr=800
    rr=rr/s


    #positioning
    painter.penup()
    painter.goto(rr,0)
    painter.pendown()



    #Draw sqaure
    for count in range(0,s):
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)
        painter.penup()
        painter.goto(-rr,0)
        painter.pendown()

#for 3

if s==3:

    #math
    rr=800
    rr=rr/s


    #positioning
    painter.penup()
    painter.goto(rr,0)
    painter.pendown()

    #Draw sqaure
    for count in range(0,1):
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)
        painter.penup()
        painter.goto(-rr,0)
        painter.pendown()
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)

        painter.penup()
        painter.goto(0,0)
        painter.pendown()
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)



#for 4

if s==4:

    #math
    rr=800
    rr=rr/6


    #positioning
    painter.penup()
    painter.goto(rr,0)
    painter.pendown()

    dd=800/2

    #Draw sqaure
    for count in range(0,1):
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)
        painter.penup()
        painter.goto(-rr,0)
        painter.pendown()
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)
        painter.penup()
        painter.goto(dd,0)
        painter.pendown()
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)
        painter.penup()
        painter.goto(-dd,0)
        painter.pendown()
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)



if s==5:

    #math
    rr=0


    #positioning
    painter.penup()
    painter.goto(rr,0)
    painter.pendown()

    dd=800/2

    #Draw sqaure

    for count in range(0,1):
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)
        rr=rr+250
        painter.penup()
        painter.goto(rr,0)
        painter.pendown()
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)
        painter.penup()
        painter.goto(-rr,0)
        painter.pendown()
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)
        rr=rr+250
        painter.penup()
        painter.goto(-rr,0)
        painter.pendown()
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)

        painter.penup()
        painter.goto(rr,0)
        painter.pendown()
        for count in range(0,4,1):
            painter.forward(90)
            painter.right(90)
