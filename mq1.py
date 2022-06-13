# num1=100
# num2=99
# if num1>num2:
#     print("bada hai")
# else:
#     print("chhota hai")

import tkinter as Tk
from turtle import *
bgcolor("black")
speed(0)
hideturtle()

for i in range(120):
    color("red")
    circle(i)
    color("orange")
    circle(i*0,8)
    right(3)
    forward(3)
done()