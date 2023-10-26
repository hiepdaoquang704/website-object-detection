import cv2
from datetime import datetime 

class Webcam():
    def __init__(self):
        self.vid=cv2.VideoCapture(0)# url to webcam
    def get_frame(self):
        if not self.vid.isOpened():
            return
        while True:
            _,img=self.vid.read()
            font =cv2.FONT_HERSHEY_SIMPLEX
            org =(50,50)
            frontScale=1
            color =(255,0,0)
            thickness=2
            img=cv2.putText(img,datetime.now().strftime("%H:%M:%S"),org,font,
                           frontScale,color,thickness,cv2.LINE_AA)
            
            yield img