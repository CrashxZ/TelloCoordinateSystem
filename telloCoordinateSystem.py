class telloC:
	def moveENU(self,x,y,z):
		if x>0:
			self.tello.right(x)
		elif x<0:
			self.tello.left(x*-1)

		if y>0:
			self.tello.forward(y)
		elif y<0:
			self.tello.back(y*-1)

		if z>0:
			self.tello.up(z)
		elif z<0:
			self.tello.down(z*-1)

	def moveNED(self,x,y,z):
		if y>0:
			self.tello.right(y)
		elif y<0:
			self.tello.left(y*-1)

		if x>0:
			self.tello.forward(x)
		elif x<0:
			self.tello.back(x*-1)

		if z>0:
			self.tello.down(z)
		elif z<0:
			self.tello.up(z*-1)


	def move(self,x,y,z):
		ENU = 1
		x=int(x*100)
		y=int(y*100)
		z=int(z*100)
		if(ENU==0):
			self.moveNED(x,y,z)
		else: 
			self.moveENU(x,y,z)

	def __init__(self, driver):
        	self.tello = driver
		# Unit = Meters
		# Delta Trajectory
