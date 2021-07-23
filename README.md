# HandTrackingController
This application lets you control any game that accepts XInputs with your hands

# requirements
This program has only been tested on python version 3.7.1


1. opencv-python
2. mediapipe
3. vgamepad

You can download them using these commands:

<code>pip install opencv-python</code>

<code>pip install mediapipe</code>

<code>pip install vgamepad</code>

# Devlog
You can watch my devlogs here:
https://youtube.com/channel/UCX6mis1jc5RIFo-A2PpwKQg

# Known issues
1. Sometimes when the image of the webcam is blurry,
the right hand can get detected as the left hand and vice versa
2. Covering multiple fingers may result in falsely detected hand gestures

An evenly lit room, an one-color background or a camera with a higher framerate should solve these issues.
If not, please contact me through my youtube account
