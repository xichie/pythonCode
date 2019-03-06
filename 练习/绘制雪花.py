import turtle
from turtle import *

# 科赫曲线
def koch(size,n):
	if n == 0:
		turtle.fd(size)
	else:
		for angle in [0,60,-120,60]:
			turtle.left(angle)
			koch(size/3, n-1)
def main():
	turtle.setup(600,600)
	turtle.pen(speed = 0, pencolor = 'blue')
	turtle.penup()
	turtle.goto(-200,100)
	turtle.pendown()
	turtle.pensize(1)
	level = 5
	koch(400,level)
	turtle.right(120)
	koch(400, level)
	turtle.right(120)
	koch(400, level)
	turtle.hideturtle()
	ts = turtle.getscreen()
	ts.getcanvas().postscript(file="./duck.eps") #.eps文件即postscript脚本

main()