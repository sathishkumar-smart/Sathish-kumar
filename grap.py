import turtle             
colors = [ "red","purple","blue","green","orange","yellow","white","brown","violet"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for i in range(360):
   my_pen.pencolor(colors[i % 9])
   my_pen.width(i/50 + 1)
   my_pen.forward(i)
   my_pen.left(65)