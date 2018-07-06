#composite transformation
# -*- coding: utf-8 -*-
from tkinter import *
from math import sin, cos, radians, pi
def draw(x1,y1,x2,y2,x3,y3):

	x1,y1=ox+x1,oy-y1
	x2,y2=ox+x2,oy-y2
	x3,y3=ox+x3,oy-y3
	w.create_polygon(x1,y1,x2,y2,x3,y3,fill='white',outline='black')

def composite(x,y,tx,ty,Sx,Sy,theta):

	T=    [[1, 0, tx],
		[0, 1, ty],
		[0, 0, 1]]

	S=    [[Sx, 0, 0],
		[0, Sy, 0],
		[0, 0, 1]]
	Rot = 	[[cos(theta), -sin(theta), 0],
      		[sin(theta), cos(theta),  0],
      		[0,              0,        1  ]]

	P =     [[x],
		[y],
		[1]]

	result1 = [[0,0,0,0],
         	[0,0,0,0],
         	[0,0,0,0]]
	result2 = [[0,0,0,0],
         	[0,0,0,0],
         	[0,0,0,0]]	
	result= [[0],
	  	 [0],
	   	 [0]]

#Matrix multiplication result=(Rot.(S.T)).P
	#Matrix multiplication result1=(S.T)
	# iterate through rows of S
	for i in range(len(S)):
		# iterate through columns of T
		for j in range(len(T[0])):
			# iterate through rows of T
			for k in range(len(T)):
				result1[i][j] += S[i][k] * T[k][j]

	#Matrix multiplication result2=Rot.(S.T)
	# iterate through rows of Rot
	for i in range(len(Rot)):
		# iterate through columns of result1 or S.T
		for j in range(len(result1[0])):
			# iterate through rows of T
			for k in range(len(result1)):
				result2[i][j] += Rot[i][k] * result1[k][j]
	print("Composite Matrix:")
	print(result2)
	#Matrix multiplication result=(Rot.(S.T)).P
	# iterate through rows of result2
	for i in range(len(result2)):
		# iterate through columns of P
		for j in range(len(P[0])):
			# iterate through rows of T
			for k in range(len(P)):
				result[i][j] += result2[i][k] * P[k][j]
	
	return result[0][0],result[1][0]

print("Enter the first point of triangle")
x1,y1=map(int,input().split())
print("Enter the second point of triangle")
x2,y2=map(int,input().split())
print("Enter the third point of triangle")
x3,y3=map(int,input().split())
print("Composite transformation")
print("1.Translation through tx,ty")
print("2.Scaling through Sx,Sy")
print("3.Rotation through theta")

print("Enter translation factor tx and ty")
tx,ty=map(int,input().split())
print("Enter scaling factor Sx and Sy")
Sx,Sy=map(float,input().split())
print("Enter value of theta in degrees")
theta=float(input())
theta=radians(theta)
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

x1t,y1t=composite(x1,y1,tx,ty,Sx,Sy,theta)
x2t,y2t=composite(x2,y2,tx,ty,Sx,Sy,theta)
x3t,y3t=composite(x3,y3,tx,ty,Sx,Sy,theta)

draw(x1t,y1t,x2t,y2t,x3t,y3t)
w.create_text(x1t+ox,oy-y1t+20,text="Triangle after composite transformation",font="Times 15 bold")

mainloop()

