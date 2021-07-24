import HandTrackingModule as htm
import cv2
import math
import sys
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class UISettings:

	WIDTH = int(config['WebcamSettings']['resolution_x'])
	HEIGHT = int(config['WebcamSettings']['resolution_y'])
	DrawHands = config.getboolean('UISettings','DrawHands')
	DrawHandPoints = config.getboolean('UISettings','DrawHandPoints')
	DrawJoysticks = config.getboolean('UISettings','DrawJoysticks')
	JoystickRadius = config.getint('UISettings','JoystickRadius')
	JoystickBorderThickness = config.getint('UISettings','JoystickBorderThickness')
	JoystickLineThickness = config.getint('UISettings','JoystickLineThickness')

	p1 = (int(3*WIDTH/4),int(3*HEIGHT/5))
	p2 = (int(WIDTH/4),int(3*HEIGHT/5))


detector = htm.HandDetector(maxHands=2)

def TrackHands(cap,draw=True):
	success, img = cap.read() # get BGR img from webcam
	img = cv2.flip(img,1) #flipping image for easier controls
	detector.findHands(img,draw=UISettings.DrawHands) # returns RGB img, displays hand landmarks, when draw=True
	# returns list of landmarks with (id, xposition, yposition)
	rightHand = detector.findPosition(img,label='Right',draw=UISettings.DrawHandPoints)
	leftHand = detector.findPosition(img,label='Left',draw=UISettings.DrawHandPoints)

	gestures, wrist1, wrist2 = getGestures(rightHand,leftHand)

	if draw:
		DrawOnScreen(img,wrist1,wrist2)

	cv2.imshow("Camera",img)
	if cv2.waitKey(1) == 27:
			cv2.destroyAllWindows()
			sys.exit(0)

	return gestures


def getGestures(rightHand,leftHand,draw=True):
	if len(rightHand) and len(leftHand):
		wrist1 , thumb1, index1, middle1, ring1 , pinky1 = rightHand
		wrist2 , thumb2, index2, middle2, ring2 , pinky2 = leftHand

		p1 = UISettings.p1
		p2 = UISettings.p2

		rightJoystick = ((wrist1[1]-p1[0])/UISettings.JoystickRadius,(wrist1[2]-p1[1])/UISettings.JoystickRadius)
		leftJoystick  = ((wrist2[1]-p2[0])/UISettings.JoystickRadius,(wrist2[2]-p2[1])/UISettings.JoystickRadius)

		t1_i1_dist = math.sqrt(int(thumb1[1]-index1[1])**2+int(thumb1[2]-index1[2])**2)
		t2_i2_dist = math.sqrt(int(thumb2[1]-index2[1])**2+int(thumb2[2]-index2[2])**2)

		t1_m1_dist = math.sqrt(int(thumb1[1]-middle1[1])**2+int(thumb1[2]-middle1[2])**2)
		t2_m2_dist = math.sqrt(int(thumb2[1]-middle2[1])**2+int(thumb2[2]-middle2[2])**2)

		t1_r1_dist = math.sqrt(int(thumb1[1]-ring1[1])**2+int(thumb1[2]-ring1[2])**2)
		t2_r2_dist = math.sqrt(int(thumb2[1]-ring2[1])**2+int(thumb2[2]-ring2[2])**2)

		t1_p1_dist = math.sqrt(int(thumb1[1]-pinky1[1])**2+int(thumb1[2]-pinky1[2])**2)
		t2_p2_dist = math.sqrt(int(thumb2[1]-pinky2[1])**2+int(thumb2[2]-pinky2[2])**2)

		gestures = {'rightHand':{'rightJoystick':rightJoystick,
								 'thumb_index':t1_i1_dist,
								 'thumb_middle':t1_m1_dist,
								 'thumb_ring':t1_r1_dist,
								 'thumb_pinky':t1_p1_dist
								 },
					'leftHand':{'leftJoystick':leftJoystick,
								 'thumb_index':t2_i2_dist,
								 'thumb_middle':t2_m2_dist,
								 'thumb_ring':t2_r2_dist,
								 'thumb_pinky':t2_p2_dist
								 }
					}

		return gestures, wrist1, wrist2

	else:
		return None,None,None


def DrawOnScreen(img,rightHand,leftHand):



	p1 = UISettings.p1
	p2 = UISettings.p2

	JoystickBorderThickness = UISettings.JoystickBorderThickness
	JoystickLineThickness = UISettings.JoystickLineThickness

	innerRadius = int(UISettings.JoystickRadius/2)

	if not rightHand==None:
		rightHand = (rightHand[1],rightHand[2])

		leftHand = (leftHand[1],leftHand[2])
		
		# draw left joystick
		if UISettings.DrawJoysticks:
			cv2.circle(img,p2,UISettings.JoystickRadius,(155,155,155),JoystickBorderThickness)
			cv2.line(img,p2,leftHand,(255,255,255),JoystickLineThickness)
			# draw right joystick
			cv2.circle(img,p1,UISettings.JoystickRadius,(155,155,155),JoystickBorderThickness)
			cv2.circle(img,p1,innerRadius,(0,255,255),2)
			cv2.line(img,p1,rightHand,(255,255,255),JoystickLineThickness)

	
	return img