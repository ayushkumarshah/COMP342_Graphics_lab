# -*- coding: utf-8 -*-
#shearing along x and y directions
from tkinter import *

def draw(x1,y1,x2,y2,x3,y3):
	x1,y1=ox+x1,oy-y1
	x2,y2=ox+x2,oy-y2
	x3,y3=ox+x3,oy-y3
	w.create_polygon(x1,y1,x2,y2,x3,y3,fill='white',outline='black')

def x_shear(x,y,Shx):

	Sh=    [[1, Shx, 0],
		[0, 1, 0],
		[0, 0, 1]]

	P =     [[x],
		[y],
		[1]]

	result= [[0],
	  	 [0],
	   	 [0]]

	#Matrix multiplication result=Sh.P
	# iterate through rows of Sh
	for i in range(len(Sh)):
		# iterate through columns of P
		for j in range(len(P[0])):
			# iterate through rows of P
			for k in range(len(P)):
				result[i][j] += Sh[i][k] * P[k][j]
	print(result)
	return result[0][0],result[1][0]

def y_shear(x,y,Shy):

	Sh=    [[1, 0, 0],
		[Shy, 1, 0],
		[0, 0, 1]]

	P =     [[x],
		[y],
		[1]]

	result= [[0],
	  	 [0],
	   	 [0]]

	#Matrix multiplication result=Sh.P
	# iterate through rows of Sh
	for i in range(len(Sh)):
		# iterate through columns of P
		for j in range(len(P[0])):
			# iterate through rows of P
			for k in range(len(P)):
				result[i][j] += Sh[i][k] * P[k][j]
	return result[0][0],result[1][0]

print("Enter the first point of triangle")
x1,y1=map(int,input().split())
print("Enter the second point of triangle")
x2,y2=map(int,input().split())
print("Enter the third point of triangle")
x3,y3=map(int,input().split())

print("Enter shearing factor Shx for x direction shear")
Shx=float(input())

print("Enter shearing factor Shy for y direction shear")
Shy=float(input())

master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
w=Canvas(master,width=canvas_width,height=canvas_height)
w.pack()
w.create_line(canvas_width/2,0,canvas_width/2,canvas_height)
w.create_line(0,canvas_height/2,canvas_width,canvas_height/2)
#origin
ox,oy=canvas_width/2,canvas_height/2

draw(x1,y1,x2,y2,x3,y3)
w.create_text(x1+ox,oy-y1+20,text="Original triangle",font="Times 15 bold")

x1x,y1x=x_shear(x1,y1,Shx)
x2x,y2x=x_shear(x2,y2,Shx)
x3x,y3x=x_shear(x3,y3,Shx)

draw(x1x,y1x,x2x,y2x,x3x,y3x)
w.create_text(x1x+ox,oy-y1x+20,text="Triangle after shearing through Shx="+str(Shx),font="Times 15 bold")

x1y,y1y=y_shear(x1,y1,Shy)
x2y,y2y=y_shear(x2,y2,Shy)
x3y,y3y=y_shear(x3,y3,Shy)

draw(x1y,y1y,x2y,y2y,x3y,y3y)
w.create_text(x1y+ox,oy-y1y+20,text="Triangle after shearing through Shy="+str(Shy),font="Times 15 bold")

mainloop()




     
