import cv2
import os

cam = cv2.VideoCapture("C:\\Users\\Lenovo\\Downloads\\WhatsApp Video 2024-01-10 at 11.52.43 AM.mp4")

frameno = 0
while(True):
   ret,frame = cam.read()
   if ret:
      # if video is still left continue creating images
      name = str(frameno) + '.jpg'
      print ('new frame captured...' + name)

      cv2.imwrite(name, frame)
      frameno += 1
   else:
      break

cam.release()
cv2.destroyAllWindows()
