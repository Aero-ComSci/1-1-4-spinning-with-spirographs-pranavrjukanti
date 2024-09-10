import turtle as trtl #Importing Turtle
painter = trtl.Turtle()

painter.speed(0)
x=10
y=90
z=0

while True:
    
    painter.forward(x)
    painter.left(90)
    
    x=x+10
    z=z+0.23
    if z>=30:
        break


wn = trtl.Screen()
wn.mainloop()


    
        




  
























wn = trtl.Screen()
wn.mainloop()
