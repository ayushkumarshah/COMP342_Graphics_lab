#mid point circle drawing algorithm
# -*- coding: utf-8 -*-

from tkinter import *

def sympoints(x,y,x_centre,y_centre):
	w.create_text(x + x_centre, y + y_centre,text='.')
	w.create_text(y + x_centre, x + y_centre,text='.')
	w.create_text(x + x_centre, -y + y_centre,text='.')
	w.create_text(y + x_centre, -x + y_centre,text='.')
	w.create_text(-y + x_centre, -x + y_centre,text='.')
	w.create_text(-x + x_centre, -y + y_centre,text='.')
	w.create_text(-x + x_centre, y + y_centre,text='.')
	w.create_text(-y + x_centre, x + y_centre,text='.')		

def midPointCircleDraw(x_centre, y_centre, r):
	x ,y=0,r
	
	#Printing the initial point on the axes after translation 
	sympoints(x,y,x_centre,y_centre)
	print(x,y)

	#Initialising the value of P
	P = 5/4 - r

	while (x <=y):
		x+=1
		#Mid-point is inside the perimeter of circle
		if (P < 0):
			P = P + 2*x + 1     
		#Mid-point is outside or on the perimeter of circle
		else:
			y-=1
			P = P + 2*x - 2*y + 1
		sympoints(x,y,x_centre,y_centre)
		print(x,y)

print("Enter centre of circle")
x,y=map(int, input().split())
print("Enter radius of circle")
r=int(input())

master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
w=Canvas(master,width=canvas_width,height=canvas_height)
w.pack()

midPointCircleDraw(x,y,r)

mainloop()




     
