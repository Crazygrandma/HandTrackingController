import configparser
import vgamepad as vg
config = configparser.ConfigParser()
config.read('config.ini')

def sendInputs(gamepad,gestures):
	WIDTH = int(config['WebcamSettings']['resolution_x'])
	sensitivity = float(config['ControlSettings']['sensitivity'])
	rightHand = gestures['rightHand']
	leftHand = gestures['leftHand']

	airrollBorderLeft = 2*WIDTH/8
	airrollBorderRight = 3*WIDTH/8

	rightHandControls = config['Controls-R']
	user_forwards_controls = rightHandControls['forward_controls']
	user_jump_controls = rightHandControls['jump_controls']
	user_boost_controls = rightHandControls['boost_controls']
	user_camera_controls = rightHandControls['camera_controls']

	leftHandControls = config['Controls-L']
	user_reverse_controls = leftHandControls['reverse_controls']
	user_drift_controls = leftHandControls['drift_controls']


	# TURNING
	turningValue = ((rightHand['wrist_pos'][1]-(3*WIDTH/4))/(0.25 * WIDTH))*sensitivity
	if turningValue >= 1:
		gamepad.left_joystick_float(x_value_float=1, y_value_float=0)
		gamepad.update()
	elif turningValue <= -1:
		gamepad.left_joystick_float(x_value_float=-1, y_value_float=0)
		gamepad.update()
	else:
		gamepad.left_joystick_float(x_value_float=turningValue, y_value_float=0)
		gamepad.update()


	# AIRROLL
	#print(int(leftHand['wrist_pos'][1]) )
	if int(leftHand['wrist_pos'][1]) <= airrollBorderLeft:
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
		gamepad.update()
	elif int(leftHand['wrist_pos'][1]) >= airrollBorderRight:
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_RIGHT)
		gamepad.update()
	else:
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_RIGHT)
		gamepad.update()


	# FORWARDS
	if int(rightHand[user_forwards_controls]) <= 255:
		gamepad.right_trigger(value=255-int(rightHand[user_forwards_controls]))
		gamepad.update()
	else:
		gamepad.right_trigger(value=0)
		gamepad.update()


	# BACKWARDS
	if int(leftHand[user_reverse_controls])<= 255:
		gamepad.left_trigger(value=255-int(leftHand[user_reverse_controls]))
		gamepad.update()
	else:
		gamepad.left_trigger(value=0)
		gamepad.update()


	# JUMP
	if int(rightHand[user_jump_controls]) <= 50:
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
		gamepad.update()
	else:
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
		gamepad.update()


	# BOOST
	if int(rightHand[user_boost_controls]) <= 50:
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		gamepad.update()
	else:
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		gamepad.update()


	# CAMERA
	if int(rightHand[user_camera_controls]) <= 50:
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
		gamepad.update()
	else:
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
		gamepad.update()


	# DRIFT
	if int(leftHand[user_drift_controls]) <= 50:
		gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
		gamepad.update()
	else:
		gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
		gamepad.update()

