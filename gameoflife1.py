import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate
from pynput.mouse import Listener
from pynput.mouse import Button, Controller
import time
mouse = Controller()

# Read mouse position
xmouse=0
ymouse=0	
count=0
taille=16
def setGame(grille):
	plt.draw()
	global count
	while count<10:
		plt.waitforbuttonpress()
	figure.canvas.mpl_disconnect(cid) #connect event to function

def voisins(k,l,grid):
	n=0
	n=grid[k+1,l]+grid[k-1,l]+grid[k,l-1]+grid[k,l+1]+grid[k-1,l-1]+grid[k+1,l-1]+grid[k+1,l+1]+grid[k-1,l+1]
	return n

def game(grid):
	temp=grid.copy()
	for k in range (0,taille-1):
		for l in range (0,taille-1):
			nbVoisins=voisins(k,l,grid)
			if grid[k,l]==1:
				if nbVoisins>3 or nbVoisins<2:
					temp[k,l]=0
			else:
				if nbVoisins==3:
					temp[k,l]=1
	return temp.copy()


def init():
	im.set_data(grid)
	setGame(grid)
	return [im]

def update(i):
	global grid,im
	grid=game(grid)
	im.set_data(grid)

	return [im]
def onclick(event):  #callback function
	global count     
	ymouse=round(event.xdata)
	xmouse=round(event.ydata)
	print(int(xmouse))
	print(int(ymouse))
	grid[int(xmouse),int(ymouse)]=1
	im.set_data(grid)
	plt.draw()
	count=count+1
   

grid=np.zeros((taille,taille))
figure,ax= plt.subplots()
im=ax.imshow(grid,cmap='gist_gray_r',vmin=0,vmax=1,animated=True)
cid = figure.canvas.mpl_connect('button_press_event', onclick) #connect event to function


ani=animate.FuncAnimation(figure,update,init_func=init,interval=500,frames=100,blit=True)
plt.show()



