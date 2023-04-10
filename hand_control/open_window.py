import cv2

class FrameStuff(object):
    cam = cv2.VideoCapture(0)
    print(cam.isOpened())
    
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)
        
    def update(self):
        while self.cam.isOpened():
            _, frame = self.cam.read()
            cv2.imshow("Main", frame)

            if cv2.waitKey(1) == ord('q'): break
            print(frame)
        
FrameStuff().update()
