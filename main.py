import cv2
import configparser
import HandController
import controller


def load_camera():
    if fastOpen:
        cap = cv2.VideoCapture(Device_Index, cv2.CAP_DSHOW)  # Open camera with fastOpen=True
    else:
        cap = cv2.VideoCapture(Device_Index)  # Open camera with fastOpen=False
    # Change the resolution of the camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

    return cap


def main():

    gamepad = controller.init_controller()

    cap = load_camera()
    while cap.isOpened():

        gestures = HandController.track_hands(cap)
        if gestures is not None:
            controller.send_inputs(gamepad, gestures)
        else:
            gamepad.reset()
            gamepad.update()


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    WIDTH = int(config['WebcamSettings']['resolution_x'])
    HEIGHT = int(config['WebcamSettings']['resolution_y'])
    fastOpen = config.getboolean('WebcamSettings', 'fastOpen')
    Device_Index = int(config['WebcamSettings']['device_index'])

    main()
