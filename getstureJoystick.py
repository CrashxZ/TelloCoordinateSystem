from easytello import tello
import telloCoordinateSystem
import socket
import ast
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 46289))
s.listen(5)
tello = tello.Tello()
T = telloCoordinateSystem.telloC(tello)
flag = 1
last_x = 0
last_y = 0
commandTime = time.time()


def transformCoordinates(temp):
    data = temp.decode()
    x = 0
    y = 0
    if data:
        #print(data)
        try:
            data = ast.literal_eval(data)
        except:
            return 0,0
        x = data[0] - 0.5
        y = data[0] - 0.5
    return x * 2, y * 2


def flyTello(x, y, z, flag, t):
    tx = -999
    # print("flag")
    if flag:
        tello.takeoff()
    if (t > 2):
        T.move(x, y, z)
        tx = time.time()
        print(t)
    return tx


conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    x, y = transformCoordinates(data)
    # print(x, y)
    gap = time.time() - commandTime
    # print(gap)
    tx = flyTello(x, y, 0, flag, gap)
    if tx != -999:
        commandTime = tx
        last_x = x
        last_y = y
    flag = 0
