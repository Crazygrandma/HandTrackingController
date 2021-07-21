import math
import cv2

def getGestures(img,rightHand,leftHand,draw=True):
	if len(rightHand) and len(leftHand):
		wrist1 , thumb1, index1, middle1, ring1 , pinky1 = rightHand
		wrist2 , thumb2, index2, middle2, ring2 , pinky2 = leftHand

		t1_i1_dist = math.sqrt(int(thumb1[1]-index1[1])**2+int(thumb1[2]-index1[2])**2)
		t2_i2_dist = math.sqrt(int(thumb2[1]-index2[1])**2+int(thumb2[2]-index2[2])**2)

		t1_m1_dist = math.sqrt(int(thumb1[1]-middle1[1])**2+int(thumb1[2]-middle1[2])**2)
		t2_m2_dist = math.sqrt(int(thumb2[1]-middle2[1])**2+int(thumb2[2]-middle2[2])**2)

		t1_r1_dist = math.sqrt(int(thumb1[1]-ring1[1])**2+int(thumb1[2]-ring1[2])**2)
		t2_r2_dist = math.sqrt(int(thumb2[1]-ring2[1])**2+int(thumb2[2]-ring2[2])**2)

		t1_p1_dist = math.sqrt(int(thumb1[1]-pinky1[1])**2+int(thumb1[2]-pinky1[2])**2)
		t2_p2_dist = math.sqrt(int(thumb2[1]-pinky2[1])**2+int(thumb2[2]-pinky2[2])**2)

		gestures = {'rightHand':{'wrist_pos':wrist1,
								 'thumb_index':t1_i1_dist,
								 'thumb_middle':t1_m1_dist,
								 'thumb_ring':t1_r1_dist,
								 'thumb_pinky':t1_p1_dist
								 },
					'leftHand':{'wrist_pos':wrist2,
								 'thumb_index':t2_i2_dist,
								 'thumb_middle':t2_m2_dist,
								 'thumb_ring':t2_r2_dist,
								 'thumb_pinky':t2_p2_dist
								 }
					}


		if draw:
			cv2.line(img, (thumb1[1],thumb1[2]),(index1[1],index1[2]),(0,255,0),2)
			cv2.line(img, (thumb1[1],thumb1[2]),(middle1[1],middle1[2]),(0,255,0),2)
			cv2.line(img, (thumb1[1],thumb1[2]),(ring1[1],ring1[2]),(0,255,0),2)
			cv2.line(img, (thumb1[1],thumb1[2]),(pinky1[1],pinky1[2]),(0,255,0),2)

		return gestures