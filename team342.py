#Program to draw Octagon/rectangle/triangle using turtle module
# pycharm editor and Jetburns IDE
#Written by Saurav Barua, Assistant professor,
#Department of Civil Engineering, Daffodil International University
#import turtle module
import turtle
turtle.speed(5)
turtle.shape('turtle')
print('Enter angle 45/90/120 degree')
a = input('angle = ')
a = int(a)
# draw octagon
if a == 45:
    print('It is an octagon')
    for i in range(10):
     turtle.forward(50)
     turtle.left(a)
    turtle.exitonclick()
# draw rectangle
elif a==90:
    print('It is a rectangle')
    for i in range(10):
        turtle.forward(50)
        turtle.left(a)
    turtle.exitonclick()
# draw triangle
elif a==120:
    print('It is a triangle')
    for i in range(10):
        turtle.forward(50)
        turtle.left(a)
    turtle.exitonclick()
#otherwise
else:
    print('Please enter valid angle')

