import cv2
import time
import configparser
import vgamepad as vg
import HandController
import controller
from importlib import reload


def loadCamera():
	if fastOpen:
		cap = cv2.VideoCapture(Device_Index,cv2.CAP_DSHOW) # Open camera with fastOpen=True
	else:
		cap = cv2.VideoCapture(Device_Index) # Open camera with fastOpen=False
	# Change the resolution of the camera
	cap.set(cv2.CAP_PROP_FRAME_WIDTH,WIDTH)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT,HEIGHT)

	return cap


def main():
	mycontroller = controller.VDS4Gamepad()
	gamepad = mycontroller.Initialise(vg)

	cap = loadCamera()
	counter = 0
	while (cap.isOpened()):
		# Uncomment the try and except block for easier debugging/developing
		# Credit to jurstu98 for this brilliant idea :)
		#try:
			if counter == 30:
				reload(HandController)
				reload(controller)
			gestures = HandController.TrackHands(cap)
			if gestures != None:
				controller.sendInputs(gamepad,gestures)
			else:
				gamepad.reset()
				gamepad.update()
		#except Exception as e:
			#print("Error",e)



if __name__ == '__main__':
	config = configparser.ConfigParser()
	config.read('config.ini')
	WIDTH = int(config['WebcamSettings']['resolution_x'])
	HEIGHT = int(config['WebcamSettings']['resolution_y'])
	fastOpen = config.getboolean('WebcamSettings','fastOpen')
	Device_Index = int(config['WebcamSettings']['device_index'])

	main()
