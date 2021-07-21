import cv2
import time
import configparser
from importlib import reload
import vgamepad as vg
import TrackToInput


def loadCamera(Device_Index,fastOpen,WIDTH,HEIGHT):
	if fastOpen:
		cap = cv2.VideoCapture(Device_Index,cv2.CAP_DSHOW) # Open camera with fastOpen=True
	else:
		cap = cv2.VideoCapture(Device_Index) # Open camera with fastOpen=False
	# Change the resolution of the camera
	cap.set(cv2.CAP_PROP_FRAME_WIDTH,WIDTH)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT,HEIGHT)

	return cap


def main():
	cap = loadCamera(Device_Index,fastOpen,WIDTH,HEIGHT)
	#counter = 0
	while (cap.isOpened()):
		# Uncomment for easier debugging/developing - credit to jurstu98 for this idea :)
		#try:
			#cTime = time.time()
			#if counter == 10:
				#reload(TrackToInput)
				#counter=0
			TrackToInput.track(cap,gamepad)
			#counter+=1
			#pTime = time.time() - cTime
			#fpsArray.append(int(1/pTime))
			#print(np.mean(fpsArray))
		#except Exception as e:
			#print("Error: ",e)



if __name__ == '__main__':
	config = configparser.ConfigParser()
	config.read('config.ini')
	WIDTH = int(config['WebcamSettings']['resolution_x'])
	HEIGHT = int(config['WebcamSettings']['resolution_y'])
	fastOpen = config.getboolean('WebcamSettings','fastOpen')
	Device_Index = int(config['WebcamSettings']['device_index'])

	# Initialise Gamepad and press buttons for wakeup

	gamepad = vg.VDS4Gamepad()


	gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_RIGHT)
	gamepad.update()
	time.sleep(1.0)
	gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_RIGHT)
	gamepad.update()
	time.sleep(1.0)

	gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_RIGHT)
	gamepad.update()
	time.sleep(1.0)
	gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_RIGHT)
	gamepad.update()
	time.sleep(1.0)

	main()