#Liang-Barsky Line Clipping Algorithm
# -*- coding: utf-8 -*-
from tkinter import *
import time

 
# Implementing Liang-Barsky algorithm
# Clipping a line from P1 = (x1, y1) to P2 = (x2, y2)
def liang_basrsky_algo(x1,y1,x2,y2):

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
	points1=[xmin+ox,oy-ymin,ox+xmax,oy-ymax]
	w.create_rectangle(points1,fill='white',outline='black')

	points2=[x1+ox,oy-y1,ox+x2,oy-y2]
	j=w.create_line(points2)
	accept=True
	dx,dy=x2-x1,y2-y1
	p=[-dx,dx,-dy,dy]
	q=[x1-xmin,xmax-x1,y1-ymin,ymax-y1]
	r=[]
	u1,u2=0,1	
	for i in range(4):
		if(p[i]==0 and q[i]<0):
			accept=false
			print("The line is outside the clip window")
			break
		else:				
			r.insert(i,q[i]/p[i])
			if(p[i]<0):
				if u1<=r[i]:
					u1=r[i]			
			else:
				if u2>=r[i]:
					u2=r[i]					
	if (accept and u1<=u2):
		x1n = x1 + u1 * dx
		y1n = y1 + u1 * dy
		x2n = x1 + u2 * dx
		y2n = y1 + u2 * dy
		print ("Line accepted from %.2f,%.2f to %.2f,%.2f" % (x1n,y1n,x2n,y2n))
		master.update()
		time.sleep(2)
		w.delete(j)
		points2=[x1n+ox,oy-y1n,ox+x2n,oy-y2n]
		w.create_line(points2)
		w.create_text(xmin+ox,oy-ymin+20,text="Line accepted from %.2f,%.2f to %.2f,%.2f" % (x1n,y1n,x2n,y2n),font="Times 15 bold")
	else:
		print("Line rejected")
		master.update()
		time.sleep(2)
		w.delete(j)
		w.create_text(xmin+ox,oy-ymin+20,text="Line rejected",font="Times 15 bold")

print("Enter the coordinates of clipping window xwmin, ywmin, xwmax, ywmax")
xmin,ymin,xmax,ymax=map(int,input().split())
print("Enter the end points of the line: x1, y1, x2, y2")
x1,y1,x2,y2=map(int,input().split())

liang_basrsky_algo(x1,y1,x2,y2)
mainloop()



