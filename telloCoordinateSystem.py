from easytello import tello 
tello = tello.Tello()

ENU = 1
# Unit = Meters
# Delta Trajectory

def moveENU(x,y,z):
	if x>0:
		tello.east(x)
	elif x<0:
		tello.west(x)

	if y>0:
		tello.forward(y)
	elif y<0:
		tello.back(y)

	if z>0:
		tello.up(z)
	elif z<0:
		tello.down(z)

def moveNED(x,y,z):
	if y>0:
		tello.east(y)
	elif y<0:
		tello.west(y)

	if x>0:
		tello.forward(x)
	elif x<0:
		tello.back(x)

	if z>0:
		tello.down(z)
	elif z<0:
		tello.up(z)


def move(x,y,y):
	x=x*100
	y=y*100
	z=z*100
	if(NED==1):
		moveNED(x,y,z)
	else 
		moveENU(x,y,z)





