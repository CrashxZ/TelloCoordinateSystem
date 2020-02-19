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
		x=int(x*100)
		y=int(y*100)
		z=int(z*100)
		#Position Calculation
		self.home_x = int(self.home_x + x)
		self.home_y = int(self.home_y + y)
		self.home_z = int(self.home_z + z)

		if(self.ENU==0):
			self.moveNED(x,y,z)
		else: 
			self.moveENU(x,y,z)


	def goHome(self):
		if(self.ENU==0):
			self.moveNED(self.home_x*-1,self.home_y*-1,self.home_z*-1)
		else: 
			self.moveENU(self.home_x*-1,self.home_y*-1,self.home_z*-1)

	def __init__(self, driver):
		self.tello = driver
		self.ENU = 1
		# Unit = Meters
		# Delta Trajectory
		self.home_x = 0
		self.home_y = 0
		self.home_z = 0
