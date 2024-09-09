import turtle as trtl #Importing Turtle
painter = trtl.Turtle()

painter.speed(0)


p=4
z=90
y=0
x=90
n=True
while n:
    painter.forward(x)
    painter.right(z)
    y=y+1
    if y%p==0:
        x=x-20
        if x<=-600:
            n=False

  


    
        




  
























wn = trtl.Screen()
wn.mainloop()
