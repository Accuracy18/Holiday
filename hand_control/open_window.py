import cv2


class FrameStuff(object):
    cam = cv2.VideoCapture('/dev/video0')
    print(cam.isOpened())
    
    cv2.namedWindow("Main Frame")
    
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)
        
    def update(self):
        while self.cam.isOpened():
            _ret, frame = self.cam.read()
            print(frame)
            
            cv2.imshow("Main Frame", frame)
        
FrameStuff().update()
