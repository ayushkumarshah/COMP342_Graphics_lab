#Cohen Sutherland Line Clipping Algorithm
# -*- coding: utf-8 -*-
from tkinter import *
import time

# Defining region codes
INSIDE = 0 #0000
LEFT = 1 #0001
RIGHT = 2 #0010
BOTTOM = 4 #0100
TOP = 8	 #1000

# Function to compute region code for a point(x,y)
def computeCode(x, y):
	code = INSIDE
	if x < xwmin:	 # to the left of rectangle
		code |= LEFT
	elif x > xwmax: # to the right of rectangle
		code |= RIGHT
	if y < ywmin:	 # below the rectangle
		code |= BOTTOM
	elif y > ywmax: # above the rectangle
		code |= TOP

	return code
 
# Implementing Cohen-Sutherland algorithm
# Clipping a line from P1 = (x1, y1) to P2 = (x2, y2)
def cohen_sutherland_algo(x1,y1,x2,y2):

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

	points2=[x1+ox,oy-y1,ox+x2,oy-y2]
	i=w.create_line(points2)

	# Compute region codes for P1, P2
	code1 = computeCode(x1,y1)
	code2 = computeCode(x2,y2)
	accept = False
	m = float(y2-y1)/(x2-x1)

	print(code1,code2)

	while True:

		# If both endpoints lie within rectangle
		if code1 == 0 and code2 == 0:
			accept = True
			print('Completely inside')
			break

		# If both endpoints are outside rectangle
		elif (code1 & code2) != 0:
			print('Completely outside')
			break

		# Some segment lies within the rectangle
		else:
			print('Partially inside')
			# Line Needs clipping
			# At least one of the points is outside, 
			# select it
			x = 1.0
			y = 1.0
			if code1 != 0:
				code_out = code1
			else:
				code_out = code2

			# Find intersection point using formulas 
			# y = y1 + slope * (x - x1) for vertical boundary 
			# x = x1 + (1 / slope) * (y - y1) for horizontal boundary
			if code_out & TOP:
		
				# point is above the clip rectangle
			
				y = ywmax
				x = x1 + (y-y1)/m
			elif code_out & BOTTOM:
			
				# point is below the clip rectangle
				y = ywmin
				x = x1 + (y-y1)/m

			elif code_out & RIGHT:
			
				# point is to the right of the clip rectangle
				x = xwmax
				y=y1+m*(x-x1)
			elif code_out & LEFT:
			
				# point is to the left of the clip rectangle
				x = xwmin
				y=y1+m*(x-x1)

			# Now intersection point x,y is found
			# We replace point outside clipping rectangle by intersection point
		
			if code_out == code1:
				x1 = x
				y1 = y
				code1 = computeCode(x1,y1)

			else:
				x2 = x
				y2 = y
				code2 = computeCode(x2,y2)

	if accept:
		print ("Line accepted from %.2f,%.2f to %.2f,%.2f" % (x1,y1,x2,y2))
		master.update()
		time.sleep(2)
		w.delete(i)
		points2=[x1+ox,oy-y1,ox+x2,oy-y2]
		i=w.create_line(points2)
		w.create_text(xwmin+ox,oy-ywmin+20,text="Line accepted from %.2f,%.2f to %.2f,%.2f" % (x1,y1,x2,y2),font="Times 15 bold")


		# Here the user can add code to display the rectangle
		# along with the accepted (portion of) lines

	else:
		print("Line rejected")
		master.update()
		time.sleep(2)
		w.delete(i)
		w.create_text(xwmin+ox,oy-ywmin+20,text="Line rejected",font="Times 15 bold")



print("Enter the coordinates of clipping window xwmin, ywmin, xwmax, ywmax")
xwmin,ywmin,xwmax,ywmax=map(int,input().split())
print("Enter the end points of the line: x1, y1, x2, y2")
x1,y1,x2,y2=map(int,input().split())

cohen_sutherland_algo(x1,y1,x2,y2)

mainloop()



