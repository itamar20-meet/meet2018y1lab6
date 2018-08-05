import turtle
while 1 == 1 :
    x=0
    y=0
    num_pts =7 
    for i in range(num_pts):
       turtle.left(360/num_pts)
       turtle.forward(100)
       turtle.goto(x+20,y+10)
   
turtle.mainloop()
