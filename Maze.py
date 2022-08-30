import pygame
import sys
import random
import time
import numpy as np
import math

pygame.init() 
ROW,COL = 5,5
width, height = 400,400 #keep width/ROW and height/COL %2 =0 !!!!
clock=pygame.time.Clock()
screen= pygame.display.set_mode((width,height))
class board:
	def __init__(self): 
		self.board = [[],[],[]]
	def draw_squares(self,screenn):
		screen.fill((255,255,255))
		for row in range(0,ROW+1,1):
			for col in range(0,COL+1,1):
				pygame.draw.rect(screen,(0,0,0),(row*(width/ROW),col*(width/ROW),width/ROW,height/COL),1)


def randomcell():
	r=random.randint(1,2*ROW-1)
	while r%2 ==0 and r!=0:
		r=random.randint(1,2*ROW-1)
	c=random.randint(1,2*COL-1)
	while c%2 ==0 and c!=0:
		c=random.randint(1,2*COL-1)
	random1=0.5*r*(width/ROW)
	random2=0.5*c*(height/COL)
	return random1,random2
#ADD CLASS HERE
def cellneighbour(s1,s2):
	#1 for going right, 2 left, 3 up and 4 down
	step=0
	while step!=1:
		step=0
		a=random.randint(1,4)
		if a==1:
			if s1<=width-((3/2)*width)/ROW:
				s1=s1+width/ROW
				step=step+1
				return s1,s2
			# else:
			# 	return s1,s2
		elif a ==2:
			if s1>=((3/2)*width)/ROW:
				s1=s1-width/ROW
				step=step+1
				return s1,s2
			# else:
			# 	return s1,s2
		elif a ==3:
			if s2>= ((3/2)*height)/COL:
				s2=s2-height/COL
				step=step+1
				return s1,s2
			# else:
			# 	return s1,s2
		elif a==4:
			if s2<=height-((3/2)*height)/COL:
				s2=s2+height/COL
				step=step+1
				return s1,s2
			# else:
			# 	return s1,s2

def updatescreen(coord):
	pygame.draw.circle(screen,(255,0,0),coord,10)
	pygame.display.update()
	pygame.draw.circle(screen,(255,255,255),coord,10)
	pygame.display.update()

def drawMaze():
	t=0
	L=[]
	LL=[]
	while len(L)<=ROW*COL-1:
		if t==0:
			n,k= randomcell()
			a,b=cellneighbour(n,k)
			updatescreen((n,k))
			c,d=n,k
			LL.append((n,k))
			LL.append((c,d))
			t=t+1
		elif t>=2:
			c,d=a,b
			a,b=cellneighbour(c,d)
			co1=(a,b)
			o=0
			while (co1 in L or (a==c and b==d)) and o<5:
				a,b=cellneighbour(c,d)
				co1=(a,b)
				o=o+1
			if o>=5:
				a,b=c,d 
		if a==c and b!=d:
			co1=(a,b)
			pygame.draw.line(screen,(255,255,255),(1.5+a-(width/(2*ROW)),((b+d)/2)),(-1.5+c+(width/(2*ROW)),((b+d)/2)),4)
			updatescreen((c,d))
			updatescreen((a,b))
			if len(L)<ROW*COL-1 or len(L)<ROW*COL-2 :
				pygame.draw.circle(screen,(255,255,255),(a,b),10)	
			LL.append((a,b))
			clock.tick(20)
			L.append(co1)
			t=t+1
		elif b==d and a!=c:
			co1=(a,b)
			pygame.draw.line(screen,(255,255,255),(((a+c)/2),1.5+b-(height/(2*COL))),(((a+c)/2),-1.5+b+(height/(2*COL))),4)
			updatescreen((c,d))
			updatescreen((a,b))
			if len(L)==ROW*COL-2:
				pygame.display.update()	
			clock.tick(10)
			L.append(co1)
			LL.append((a,b))
			t=t+1
		else:
			r=len(LL)-1
			if r>0:
				a,b=LL[r]
				LL.remove(LL[r])
	return screen
				
b=board()
b.draw_squares(screen)
drawMaze()

running = True
while running:
  	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	    	running = False
	    if running == False:
	    	pygame.quit()
