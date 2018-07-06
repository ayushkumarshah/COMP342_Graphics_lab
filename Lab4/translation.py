#translation
# -*- coding: utf-8 -*-
from tkinter import *

def draw(x1,y1,x2,y2,x3,y3):

	x1,y1=ox+x1,oy-y1
	x2,y2=ox+x2,oy-y2
	x3,y3=ox+x3,oy-y3
	w.create_polygon(x1,y1,x2,y2,x3,y3,fill='white',outline='black')

def translation(x,y,tx,ty):

	T=    [[1, 0, tx],
		[0, 1, ty],
		[0, 0, 1]]

	P =     [[x],
		[y],
		[1]]

	result= [[0],
	  	 [0],
	   	 [0]]

#Matrix multiplication result=T.P
	# iterate through rows of T
	for i in range(len(T)):
		# iterate through columns of P
		for j in range(len(P[0])):
			# iterate through rows of P
			for k in range(len(P)):
				result[i][j] += T[i][k] * P[k][j]

	return result[0][0],result[1][0]

print("Enter the first point of triangle")
x1,y1=map(int,input().split())
print("Enter the second point of triangle")
x2,y2=map(int,input().split())
print("Enter the third point of triangle")
x3,y3=map(int,input().split())

print("Enter translation factor tx and ty")
tx,ty=map(int,input().split())

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

x1t,y1t=translation(x1,y1,tx,ty)
x2t,y2t=translation(x2,y2,tx,ty)
x3t,y3t=translation(x3,y3,tx,ty)

draw(x1t,y1t,x2t,y2t,x3t,y3t)
w.create_text(x1t+ox,oy-y1t+20,text="Triangle after translation through ("+str(tx)+","+str(ty)+")",font="Times 15 bold")

mainloop()

