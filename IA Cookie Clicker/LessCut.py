import pyautogui as pyg
from Init_Big_Cookie import InitCoordsBigCookie
import keyboard as key
import numpy as np
import cv2
from time import sleep, time

sleep(2)
# Point(x=1632, y=290)
# Point(x=1641, y=1017)

screenshot = np.array(pyg.screenshot(region=(1632, 290, 10, 727)))
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)

low = np.array([50, 100, 100])
upper = np.array([70, 255, 255])

mask = cv2.inRange(screenshot, low, upper)
coord_white = np.argwhere(mask == 255)

buy_x, buy_y = coord_white[0][0]+1632, coord_white[0][1]+290
pyg.moveTo(buy_x, buy_y)

cv2.imshow('Computer Vision', mask)
cv2.waitKey(0)
