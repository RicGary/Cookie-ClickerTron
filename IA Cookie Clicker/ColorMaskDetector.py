import pyautogui as pyg
from Init_Big_Cookie import InitCoordsBigCookie
import keyboard as key
import numpy as np
import cv2
import time


img = cv2.imread('Imagens/Cookie Clicker2.JPG')
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

low = np.array([50, 100, 100])
upper = np.array([70, 255, 255])

mask = cv2.inRange(hsv, low, upper)

result = cv2.bitwise_and(img, img, mask=mask)

coord_white = np.argwhere(mask == 255)


# print(coord_white[0][0], coord_white[0][1])
# pyg.moveTo(coord_white[0][1], coord_white[0][0])

cv2.imshow('test', mask)
cv2.waitKey(0)