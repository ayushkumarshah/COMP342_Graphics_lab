#Sutherland–Hodgman Polygon Clipping Algorithm
# -*- coding: utf-8 -*-
from tkinter import *
import time
import math

def left_clipper(x1, y1, x2, y2):
	if x2 - x1 != 0:
		m = (y2 - y1)/(x2 - x1)
	else:
		m = math.inf
	if (x1 > xwmin) and (x2 > xwmin): #wholly inside
		x1 = x1
		y1 = y1
		x2 = x2
		y2 = y2
	elif (x1 < xwmin) and (x2 > xwmin): #outside to inside
		y1 = y1 + (m*(xwmin - x1))
		x1 = xwmin
		x2 = x2
		y2 = y2
	elif (x1 < xwmin) and (x2 < xwmin): #wholly outside
		pass
	elif (x1 > xwmin) and (x2 < xwmin): #inside to outside
		x1 = x1
		y1 = y1
		x2 = xwmin
		y2 = y1 + (m*(x2 - x1))
	return x1, y1, x2, y2


def bottom_clipper(x1, y1, x2, y2):
	if x2 - x1 != 0:
		m = (y2 - y1)/(x2 - x1)
	else:
		m = math.inf
	if (y1 > ywmin) and (y2 > ywmin): #wholly inside
		x1 = x1
		y1 = y1
		x2 = x2
		y2 = y2
	elif (y1 < ywmin) and (y2 > ywmin): #outside inside
		x1 = x1 + ((ywmin - y1)/m)
		y1 = ywmin
		x2 = x2
		y2 = y2
	elif (y1 < ywmin) and (y2 < ywmin): #wholly outside
		pass
	elif (y1 > ywmin) and (y2 < ywmin): #inside outside
		x1 = x1
		y1 = y1
		y2 = ywmin
		x2 = x1 + ((y2 - y1)/m)
	return x1, y1, x2, y2


def right_clipper(x1, y1, x2, y2):
	if x2 - x1 != 0:
		m = (y2 - y1)/(x2 - x1)
	else:
		m = math.inf
	if (x1 < xwmax) and (x2 < xwmax): #wholly inside
		x1 = x1
		y1 = y1
		x2 = x2
		y2 = y2
	elif (x1 > xwmax) and (x2 < xwmax): #outside inside		
		y1 = y1 + (m*(xwmax - x1))
		x1 = xwmax		
		x2 = x2
		y2 = y2
	elif (x1 > xwmax) and (x2 > xwmax): #wholly outside
		pass
	elif (x1 < xwmax) and (x2 > xwmax): #inside outside
		x1 = x1
		y1 = y1
		x2 = xwmax
		y2 = y1 + (m*(x2 - x1))
	return x1, y1, x2, y2


def top_clipper(x1, y1, x2, y2):
	if x2 - x1 != 0:
		m = (y2 - y1)/(x2 - x1)
	else:
		m = math.inf
	if (y1 < ywmax) and (y2 < ywmax): #wholly inside
		x1 = x1
		y1 = y1
		x2 = x2
		y2 = y2
	elif (y1 > ywmax) and (y2 < ywmax): #outside inside		
		x1 = x1 + ((ywmax - y1)/m)
		y1 = ywmax		
		x2 = x2
		y2 = y2
	elif (y1 > ywmax) and (y2 > ywmax): #wholly outside
		pass
	elif (y1 < ywmax) and (y2 > ywmax): #inside outside
		x1 = x1
		y1 = y1
		y2 = ywmax
		x2 = x1 + ((y2 - y1)/m)
	return x1, y1, x2, y2 

def update(x1,y1,x2,y2,x2o,y2o,x3,y3,x3o,y3o,x1o,y1o):
	master.update()
	time.sleep(2)
	w.delete("all")
	w.create_line(canvas_width/2,0,canvas_width/2,canvas_height)
	w.create_line(0,canvas_height/2,canvas_width,canvas_height/2)
	points1=[xwmin+ox,oy-ywmin,ox+xwmax,oy-ywmax]
	w.create_rectangle(points1,fill='white',outline='black')
	w.create_line(x1+ox,oy-y1,ox+x2,oy-y2)
	w.create_line(ox+x2o,oy-y2o,ox+x3,oy-y3)
	w.create_line(ox+x3o,oy-y3o,ox+x1o,oy-y1o)


# Implementing Sutherland–Hodgman Algorithm

def sutherland_hodgman_algo(x1,y1,x2,y2,x3,y3):
	x1o,y1o,x2o,y2o,x3o,y3o=x1,y1,x2,y2,x3,y3
	#left_clipper

	x1, y1, x2, y2 = left_clipper(x1, y1, x2, y2)
	x2o, y2o, x3, y3 = left_clipper(x2o, y2o, x3, y3)
	x3o, y3o, x1o, y1o = left_clipper(x3o, y3o, x1o, y1o)
	update(x1,y1,x2,y2,x2o,y2o,x3,y3,x3o,y3o,x1o,y1o)

	#top_clipper
	x1, y1, x2, y2 = top_clipper(x1, y1, x2, y2)
	x2o, y2o, x3, y3 = top_clipper(x2o, y2o, x3, y3)
	x3o, y3o, x1o, y1o = top_clipper(x3o, y3o, x1o, y1o)
	update(x1,y1,x2,y2,x2o,y2o,x3,y3,x3o,y3o,x1o,y1o)

	#right_clipper
	x1, y1, x2, y2 = right_clipper(x1, y1, x2, y2)
	x2o, y2o, x3, y3 = right_clipper(x2o, y2o, x3, y3)
	x3o, y3o, x1o, y1o = right_clipper(x3o, y3o, x1o, y1o)
	update(x1,y1,x2,y2,x2o,y2o,x3,y3,x3o,y3o,x1o,y1o)

	#bottom_clipper
	x1, y1, x2, y2 = bottom_clipper(x1, y1, x2, y2)
	x2o, y2o, x3, y3 = bottom_clipper(x2o, y2o, x3, y3)
	x3o, y3o, x1o, y1o = bottom_clipper(x3o, y3o, x1o, y1o)
	update(x1,y1,x2,y2,x2o,y2o,x3,y3,x3o,y3o,x1o,y1o)

print("Enter the coordinates of clipping window xwmin, ywmin, xwmax, ywmax")
xwmin,ywmin,xwmax,ywmax=map(int,input().split())
print("Enter the end points of the polygon: x1, y1, x2, y2, x3, y3")
x1,y1,x2,y2,x3,y3=map(int,input().split())

master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
w=Canvas(master,width=canvas_width,height=canvas_height)
w.pack()
w.create_line(canvas_width/2,0,canvas_width/2,canvas_height)
w.create_line(0,canvas_height/2,canvas_width,canvas_height/2)
#origin
ox,oy=canvas_width/2,canvas_height/2

#clipping window
points1=[xwmin+ox,oy-ywmin,ox+xwmax,oy-ywmax]
w.create_rectangle(points1,fill='white',outline='black')

points2=[x1+ox,oy-y1,ox+x2,oy-y2,ox+x3,oy-y3]
j=w.create_polygon(points2,fill='white',outline='black')

sutherland_hodgman_algo(x1,y1,x2,y2,x3,y3)
mainloop()



