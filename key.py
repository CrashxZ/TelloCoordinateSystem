import numpy as np
import cv2
import socket

# Capturing video through webcam
webcam = cv2.VideoCapture(0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 46289
try:
    s.connect(("localhost", port))
except:
    print("Error")
# Start a while loop 
while (1):

    # Reading the video from the 
    # webcam in image frames 
    _, imageFrame = webcam.read()
    # Convert the imageFrame in  
    # BGR(RGB color space) to  
    # HSV(hue-saturation-value) 
    # color space 
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Set range for Tracker color and
    # define mask 
    # tracker
    tracker_lower = np.array([17, 182, 100], np.uint8)
    tracker_upper = np.array([100, 255, 255], np.uint8)
    tracker_mask = cv2.inRange(hsvFrame, tracker_lower, tracker_upper)

    # Morphological Transform, Dilation 
    # for each color and bitwise_and operator 
    # between imageFrame and mask determines 
    # to detect only that particular color 
    kernal = np.ones((5, 5), "uint8")

    # For Tracker color
    tracker_mask = cv2.dilate(tracker_mask, kernal)
    res_tracker = cv2.bitwise_and(imageFrame, imageFrame,
                                  mask=tracker_mask)

    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(tracker_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 0, 255), 2)

            cv2.putText(imageFrame, "Joystick", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))
            joy_x = (x + w / 2)/640;
            joy_y = (y + h / 2)/480;

            formatted_string = "[" + str(joy_x) + "," + str(joy_y) + "]"
            try:
                s.sendto(str.encode(formatted_string), ("localhost", port))
            except:
                print("Error")
                continue

            # Program Termination
    cv2.imshow("Tracker", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        s.close()
        cap.release()
        cv2.destroyAllWindows()
        break
