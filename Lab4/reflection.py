#reflection
# -*- coding: utf-8 -*-
from tkinter import *

def draw(x1,y1,x2,y2,x3,y3):

	x1,y1=ox+x1,oy-y1
	x2,y2=ox+x2,oy-y2
	x3,y3=ox+x3,oy-y3
	w.create_polygon(x1,y1,x2,y2,x3,y3,fill='white',outline='black')	

def reflection(x,y):
	Refx =     [[1, 0, 0],
		[0,-1, 0],
		[0, 0, 1]]

	Refy=    [[-1, 0, 0],
		[0, 1, 0],
		[0, 0, 1]]

	P =     [[x],
		[y],
		[1]]

	resultx = [[0],
	  	 [0],
	   	 [0]]

	resulty = [[0],
	  	 [0],
	   	 [0]]

#Matrix multiplication resultx=Refx.P
	# iterate through rows of Refx
	for i in range(len(Refx)):
		# iterate through columns of P
		for j in range(len(P[0])):
			# iterate through rows of P
			for k in range(len(P)):
				resultx[i][j] += Refx[i][k] * P[k][j]

#Matrix multiplication resulty=Refy.P
	# iterate through rows of Refy
	for i in range(len(Refy)):
		# iterate through columns of P
		for j in range(len(P[0])):
			# iterate through rows of P
			for k in range(len(P)):
				resulty[i][j] += Refy[i][k] * P[k][j]

	return resultx[0][0],resultx[1][0], resulty[0][0],resulty[1][0]

print("Enter the first point of triangle")
x1,y1=map(int,input().split())
print("Enter the second point of triangle")
x2,y2=map(int,input().split())
print("Enter the third point of triangle")
x3,y3=map(int,input().split())

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

x1x,y1x,x1y,y1y=reflection(x1,y1)
x2x,y2x,x2y,y2y=reflection(x2,y2)
x3x,y3x,x3y,y3y=reflection(x3,y3)

draw(x1x,y1x,x2x,y2x,x3x,y3x)
w.create_text(x1x+ox,oy-y1x-20,text="Triangle after reflection about x axis",font="Times 15 bold")

draw(x1y,y1y,x2y,y2y,x3y,y3y)
w.create_text(x1y+ox,oy-y1y+20,text="Triangle after reflection about y axis",font="Times 15 bold")

mainloop()




     
