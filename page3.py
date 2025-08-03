import random
from tkinter import messagebox
from typing import Any

import cv2
import cvzone
from cv2 import Mat
from cvzone.HandTrackingModule import HandDetector
import time

from numpy import ndarray, dtype, generic

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)
timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [AI, Player]s

while True:
    imgBG = cv2.imread("Resources/BG.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    # Find Hands
    hands, img = detector.findHands(imgScaled)  # with draw

    if startGame and stateResult is False:

        timer = time.time() - initialTime
        cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 255, 255), 4)

        if timer > 3:
            stateResult = True
            timer = 0

            if hands:
                playerMove = None
                hand = hands[0]
                fingers = detector.fingersUp(hand)
                if fingers == [0, 0, 0, 0, 0]:
                    playerMove = 1
                if fingers == [1, 1, 1, 1, 1]:
                    playerMove = 2
                if fingers == [0, 1, 1, 0, 0]:
                    playerMove = 3
                if fingers == [0, 1, 0, 0, 0]:
                    playerMove = 4

                randomNumber = random.randint(1, 4)
                imgAI= cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                # Player Wins
                if (playerMove == 1 and randomNumber == 4) or \
                        (playerMove == 2 and randomNumber == 1) or \
                        (playerMove == 3 and randomNumber == 2) or \
                        (playerMove == 4 and randomNumber == 3) or \
                        (playerMove == 2 and randomNumber == 4):
                    scores[1] += 1

                # AI Wins
                if (playerMove == 3 and randomNumber == 4) or \
                        (
                                playerMove == 1 and randomNumber == 2) or \
                        (playerMove == 2 and randomNumber == 3) or \
                        (playerMove == 4 and randomNumber == 1) or \
                        (playerMove == 4 and randomNumber == 2):

                    scores[0] += 1

    imgBG[234:654, 795:1195] = imgScaled

    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    # cv2.imshow("Image", img)
    cv2.imshow("BG", imgBG)
    # cv2.imshow("Scaled", imgScaled)

    key = cv2.waitKey(1)

    if key == ord('y'):
        startGame = True
        initialTime: float = time.time()
        stateResult = False
    if key == ord('n'):
        break
    if scores[0] == 5:
        print("AI wins", scores[0], "points")
        messagebox.showinfo("GAME OVER", "         AI WINS        ")
        break

    if scores[1] == 5:
        print("player wins", scores[1], "points")
        messagebox.showinfo("GAME OVER", "         PLAYER WINS       ")
        break