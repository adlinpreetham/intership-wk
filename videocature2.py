import cv2
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("failed to open video capture.")
    exit()
while True:
    ret,frame=cap.read()
    if not ret:
        print("Failed to capture Frame.")
        break
    cv2.imshow("Video capture",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
