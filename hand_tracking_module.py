import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.results = None

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,
                                        self.maxHands,
                                        self.detectionCon,
                                        self.trackCon
                                        )
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB.flags.writeable = False
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def find_position(self, img, label, draw=True, color=(255, 0, 255), lm_Index_List=(0, 4, 8, 12, 16, 20)):
        landmark_list = []
        if self.results.multi_hand_landmarks:
            if len(self.results.multi_hand_landmarks) == 2:
                for idx, lm in enumerate(self.results.multi_hand_landmarks):
                    lbl = self.results.multi_handedness[idx].classification[0].label
                    if lbl == label:
                        my_hand = self.results.multi_hand_landmarks[idx]
                        lms = my_hand.landmark
                        for i in lm_Index_List:
                            h, w, c = img.shape
                            cx, cy = int(lms[i].x * w), int(lms[i].y * h)
                            landmark_list.append([i, cx, cy])
                            if draw:
                                cv2.circle(img, (cx, cy), 7, color, cv2.FILLED)

            return landmark_list

        return landmark_list
