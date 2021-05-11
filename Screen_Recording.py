import datetime
from PIL import ImageGrab             ### PIL - Pillow, which is to Capture or Grab the Screen
import numpy as np
import cv2
from win32api import GetSystemMetrics

## to get system resolution dynamically
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

## To make a dynamic Output name 
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

## For Continuosly capturing the video, we using while loop
while (1):
    image = ImageGrab.grab(bbox=(0, 0, width, height))
    image_np = np.array(image)
    image_final = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("Secret Capture", image_final)
    captured_video.write(image_final)
    
    if cv2.waitKey(10) == ord('s'):     ### "s" is to stop the recording
        break 
