'''
Documentation: https://google.github.io/mediapipe/solutions/hands.html
'''

import cv2
import mediapipe as mp
import pyautogui
from math import dist

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1)
utils = mp.solutions.drawing_utils
screen_height, screen_width = pyautogui.size()
indexy = 0
textCol = (0, 0, 0)
x1, y1 = 15, 50

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    ot = hand_detector.process(rgb_frame)
    hands = ot.multi_hand_landmarks
    if hands:
        for hand in hands:
            # utils.draw_landmarks(frame, hand)
            ld = hand.landmark
            fingers = [0, 0, 0, 0, 0]
            col = (0, 0, 0)
            for id, landmark in enumerate(ld):
                # print(id)
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)

                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 0))
                    fingers[0] = [x, y]

                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 0))

                    fingers[1] = [x, y]

                if id == 12:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 0))

                    fingers[2] = [x, y]

                if id == 16:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 0))

                    fingers[3] = [x, y]

                if id == 20:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 0))

                    fingers[4] = [x, y]

                # ?Gestures start----------------------------------------------
                try:
                    # Checking the distance between the thumb and index finger
                    IndexThumbGap = dist(fingers[1], fingers[0])
                    MiddleThumbGap = dist(fingers[2], fingers[0])
                    RingThumbGap = dist(fingers[3], fingers[0])
                    PinkyThumbGap = dist(fingers[4], fingers[0])
                    # print(gap)

                    if(
                        all(i < fingers[0][1]-50 for i in (fingers[2][1], fingers[3][1], fingers[4][1]))

                        and
                        any(i > 50 for i in (MiddleThumbGap, RingThumbGap, PinkyThumbGap))
                    ):
                        '''check if middle ring and pinky are above thumb AND open hand'''
                        print('open hand')
                        break

                    if(IndexThumbGap < 30 and fingers[0][1] > fingers[1][1]):   #check if index is above thumb
                        if all(i < 30 for i in (MiddleThumbGap, RingThumbGap, PinkyThumbGap)):  # checks if all fingers are together
                            pyautogui.press('playpause')
                            # pyautogui.PAUSE=1
                            print('PAUSE')
                            break

                        print('down')
                        pyautogui.press('volumedown')  # todo

                        label = 'Volume down'

                        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 1.5, 1)
                        cv2.rectangle(frame, (x1, y1 - 20), (x1 + w+5, y1), (255, 255, 255), -1)
                        cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, textCol)

                        col = (255, 0, 0)

                    elif(IndexThumbGap > 100):
                        print('up')
                        pyautogui.press('volumeup')  # todo

                        label = 'Volume up'

                        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 1.5, 1)
                        cv2.rectangle(frame, (x1, y1 - 20), (x1 + w+5, y1), (255, 255, 255), -1)
                        cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, textCol)

                        col = (0, 255, 0)

                    else:
                        label = 'Neutral'

                        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 1.5, 1)
                        cv2.rectangle(frame, (x1, y1 - 20), (x1 + w+5, y1), (255, 255, 255), -1)
                        cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, textCol)

                        col = (0, 0, 0)

                    cv2.line(frame, fingers[0], fingers[1], color=col, thickness=2)
                    break

                except:
                    pass

    cv2.imshow('Gestures', frame)
    cv2.waitKey(1)
