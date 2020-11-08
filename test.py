from easytello import tello
from telloCoordinateSystem  import telloC
import time


tello = tello.Tello()
T = telloC(tello)
tello.streamon()
print(tello.get_battery())
start = time.time()
tello.takeoff()
while(True):
    T.move(0.5,0,0)
    T.move(0,0.5,0)
    T.move(-0.5, 0, 0)
    T.move(0, -0.5, 0)
    print(tello.get_time())
    print(tello.get_battery())
