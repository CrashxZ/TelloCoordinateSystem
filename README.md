# TelloCoordinateSystem
ENU/ NED coordinate system for tello 
Usage Example

from easytello import tello 
from telloCoordinateSystem import telloC
tello = tello.Tello()#initialize tello

tello.takeoff()
telloS = telloC(tello) #initialise Tello Coordinate System
telloS.move(0,0,0.5) # use the tello Coordinate System object
telloS.move(0,0,-0.5)
tello.land()


#Syntax : telloS.move(x,y,z)
# note these are delta coordinates, ie or the change in coordinates.
