#mid point ellipse drawing algorithm
# -*- coding: utf-8 -*-

from tkinter import *

def sympoints(x,y,x_centre,y_centre):
	w.create_text(x + x_centre, y + y_centre,text='.')
	w.create_text(x + x_centre, -y + y_centre,text='.')
	w.create_text(-x + x_centre, -y + y_centre,text='.')
	w.create_text(-x + x_centre, y + y_centre,text='.')		

def midPointEllipseDraw(x_centre, y_centre, rx,ry):
	x ,y=0,ry
	
	#Printing the initial point on the axes after translation 
	sympoints(x,y,x_centre,y_centre)
	print (x,y)

	#Region 1
	#Initialising the value of P1 
	P1 = ry**2+(1/4)*(rx**2)-(rx**2)*ry

	while (2*(ry**2)*x<2*(rx**2)*y):
		x+=1
		#Mid-point is inside the perimeter of ellipse
		if (P1 < 0):
			P1 = P1 + 2*(ry**2)*x+(ry**2)     
		#Mid-point is outside or on the perimeter of circle
		else:
			y-=1
			P1 = P1 + 2*(ry**2)*x-2*(rx**2)*y+ry**2
		sympoints(x,y,x_centre,y_centre)
		print (x,y)
	#Region 2
	P2 = ((x+1/2)**2)*(ry**2)+(rx**2)*((y-1)**2)-(rx**2)*(ry**2)

	while (y!=0):
		y-=1
		#Mid-point is inside the perimeter of ellipse
		if (P2 < 0):  
			x+=1
			P2 = P2 + 2*(ry**2)*x-2*(rx**2)*y+rx**2  
		#Mid-point is outside or on the perimeter of circle
		else:
			P2 = P2 - 2*(rx**2)*y+rx**2 
		sympoints(x,y,x_centre,y_centre)
		print(x,y)

print("Enter centre of ellipse")
x,y=map(int, input().split())
print("Enter radii rx and ry of ellipse")
rx,ry=map(int, input().split())

master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
w=Canvas(master,width=canvas_width,height=canvas_height)
w.pack()

midPointEllipseDraw(x,y,rx,ry)

mainloop()




     
