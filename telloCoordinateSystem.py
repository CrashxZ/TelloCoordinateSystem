from easytello import tello 
tello = tello.Tello()

ENU = 1
# Unit = Meters
# Delta Trajectory



def moveENU(x,y,z):
	if x>0:
		tello.right(x)
	elif x<0:
		tello.left(x*-1)

	if y>0:
		tello.forward(y)
	elif y<0:
		tello.back(y*-1)

	if z>0:
		tello.up(z)
	elif z<0:
		tello.down(z*-1)

def moveNED(x,y,z):
	if y>0:
		tello.right(y)
	elif y<0:
		tello.left(y*-1)

	if x>0:
		tello.forward(x)
	elif x<0:
		tello.back(x*-1)

	if z>0:
		tello.down(z)
	elif z<0:
		tello.up(z*-1)


def move(x,y,z):
	x=int(x*100)
	y=int(y*100)
	z=int(z*100)
	if(ENU==0):
		moveNED(x,y,z)
	else: 
		moveENU(x,y,z)
