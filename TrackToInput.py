import HandTrackingModule as htm
import controller
import configparser
import HandGestures
from importlib import reload
import cv2
import sys
config = configparser.ConfigParser()
config.read('config.ini')
WIDTH = int(config['WebcamSettings']['resolution_x'])
HEIGHT = int(config['WebcamSettings']['resolution_y'])
DrawOnScreen = config.getboolean('DebugSettings','DrawOnScreen')
BorderThickness = int(config['DebugSettings']['BorderThickness'])


airrollBorderLeft = int(2*WIDTH/8)
airrollBorderRight = int(3*WIDTH/8)
#reload(htm)
detector = htm.HandDetector(maxHands=2)

def track(cap,gamepad,draw=True):
	success, img = cap.read() # get BGR img from webcam
	img = cv2.flip(img,1) #flipping image for easier controls
	detector.findHands(img,draw=False) # returns RGB img, displays hand landmarks, when draw=True
	# returns list of landmarks with (id, xposition, yposition)
	rightHand = detector.findPosition(img,label='Right',draw=True)
	leftHand = detector.findPosition(img,label='Left',draw=True)

	# Code for defining hand gestures
	gestures = HandGestures.getGestures(img,rightHand,leftHand,draw=False) # returns dict of distances

	# and sending virtual inputs
	if gestures != None:
		controller.sendInputs(gamepad,gestures)
	else:
		gamepad.reset()
		gamepad.update()

	if DrawOnScreen:

		cv2.rectangle(img,(airrollBorderLeft,0),(airrollBorderRight,HEIGHT),(0,0,255),2)


	# Show img
	cv2.imshow("Image",img)
	


	if cv2.waitKey(1) == 27:
		gamepad.reset()
		gamepad.update()
		cv2.destroyAllWindows()
		sys.exit()