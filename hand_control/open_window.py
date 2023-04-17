from twisted.internet.protocol import DatagramProtocol

from twisted.application.service import Application
from twisted.application.internet import MulticastServer
#from twisted.application.

from twisted.internet import reactor
from twisted.internet.task import LoopingCall

import cv2, json#, mediapipe as mp, tensorflow as tf

class FrameStuff(DatagramProtocol):
    cam = cv2.VideoCapture(0)
    #hands = mp_hands.Hands()
    #mp_drawing = mp.solutions.drawing_utils
    #mp_drawing_styles = mp.solutions.drawing_styles
    #mp_hands = mp.solutions.hands
    
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)
         
    def startProtocol(self):
        self.transport.setTTL(5)
        self.transport.joinGroup("228.0.0.5")
        
        print(self.cam.isOpened())
        self.loops = LoopingCall(self.update_x)
        self.loops.start(0.05)
        
    def hand_track_motion(self, frame):
        result=self.hands.process(frame)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                        
    def update_x(self):
        if self.cam.isOpened():
            _, frame = self.cam.read()
            
            cv2.imshow("Main", frame)

            if cv2.waitKey(1) == ord('q'):
                self.loops.stop()
                self.cam.release()
                cv2.destroyAllWindows()
                reactor.stop()
            self.transport.write(b'something\n', ("228.0.0.5", 4007))
            
    def datagramReceived(self, data, addr):
        data = json.dumps(data.decode().replace('\n',''))
        
service = MulticastServer(port=4007, protocol=FrameStuff())
application = Application('strpoerts')

service.setServiceParent(application)
