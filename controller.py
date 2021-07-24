import configparser
import time
import vgamepad as vg
config = configparser.ConfigParser()
config.read('config.ini')

class Values:

	WIDTH = int(config['WebcamSettings']['resolution_x'])
	minFingerDistance = config.getint('ControlSettings','minFingerDistance')
	#sensitivity = float(config['ControlSettings']['sensitivity'])
	rightHandControls = config['Controls-R']
	user_forwards_controls = rightHandControls['forward_controls']
	user_jump_controls = rightHandControls['jump_controls']
	user_boost_controls = rightHandControls['boost_controls']
	user_camera_controls = rightHandControls['camera_controls']
	leftHandControls = config['Controls-L']
	user_reverse_controls = leftHandControls['reverse_controls']
	user_drift_controls = leftHandControls['drift_controls']

class VDS4Gamepad:

	def Initialise(self,vg):
		# Initialise Gamepad and press buttons for wakeup
		print("Connecting controller...")
		time.sleep(3.0)
		gamepad = vg.VDS4Gamepad()
		print("Initialising controller...")
		time.sleep(3.0)
		gamepad.left_joystick_float(x_value_float=0, y_value_float=0)
		gamepad.update()
		time.sleep(1.0)
		gamepad.left_joystick_float(x_value_float=0, y_value_float=-1)
		gamepad.update()
		time.sleep(1.0)
		print("Controller ready!")

		return gamepad



def sendInputs(gamepad,gestures):
	rightHand = gestures['rightHand']
	leftHand = gestures['leftHand']

	#sensFactor = (Values.sensitivity*3.5)/Values.WIDTH

	# TURNING
	leftJoystick_X = leftHand['leftJoystick'][0]
	leftJoystick_Y = leftHand['leftJoystick'][1]

	if leftJoystick_X >= 1:
		gamepad.left_joystick_float(x_value_float=1, y_value_float=leftJoystick_Y)
		gamepad.update()
	elif leftJoystick_X <= -1:
		gamepad.left_joystick_float(x_value_float=-1, y_value_float=leftJoystick_Y)
		gamepad.update()
	elif leftJoystick_Y <= -1:
		gamepad.left_joystick_float(x_value_float=leftJoystick_X, y_value_float=1)
		gamepad.update()
	elif leftJoystick_Y >= 1:
		gamepad.left_joystick_float(x_value_float=leftJoystick_X, y_value_float=-1)
		gamepad.update()
	else:
		gamepad.left_joystick_float(x_value_float=leftJoystick_X, y_value_float=leftJoystick_Y)
		gamepad.update()

	rightJoystick_X = rightHand['rightJoystick'][0]
	rightJoystick_Y = rightHand['rightJoystick'][1]


	# AIRROLL
	if rightJoystick_X >= 0.5:
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
		gamepad.update()
	elif rightJoystick_X <= -0.5:
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
		gamepad.update()
	else:
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
		gamepad.update()

	# FORWARDS
	if int(rightHand[Values.user_forwards_controls]) <= 255:
		gamepad.right_trigger(value=255-int(rightHand[Values.user_forwards_controls]))
		gamepad.update()
	else:
		gamepad.right_trigger(value=0)
		gamepad.update()

	# BACKWARDS
	if int(leftHand[Values.user_reverse_controls])<= 255:
		gamepad.left_trigger(value=255-int(leftHand[Values.user_reverse_controls]))
		gamepad.update()
	else:
		gamepad.left_trigger(value=0)
		gamepad.update()

	# JUMP
	if int(rightHand[Values.user_jump_controls]) <= Values.minFingerDistance:
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
		gamepad.update()
	else:
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
		gamepad.update()

	# BOOST
	if int(rightHand[Values.user_boost_controls]) <= Values.minFingerDistance:
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		gamepad.update()
	else:
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		gamepad.update()

	# CAMERA
	if int(rightHand[Values.user_camera_controls]) <= Values.minFingerDistance:
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
		gamepad.update()
	else:
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
		gamepad.update()

	# DRIFT
	if int(leftHand[Values.user_drift_controls]) <= Values.minFingerDistance:
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
		gamepad.update()

