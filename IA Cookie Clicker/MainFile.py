import pyautogui as pyg
from Init_Big_Cookie import InitCoordsBigCookie
import keyboard as key
import numpy as np
import cv2
from time import sleep, time


start = InitCoordsBigCookie('Imagens/Cookie Clicker.JPG', 'Imagens/InitCookie.JPG')
x_init, y_init = start

start_time = time()
while True:
    if key.is_pressed('q'):
        while True:

            pyg.click(x_init, y_init)

            if pyg.pixel(1527, 106) != (107, 62, 37):
                pyg.click(1527, 106)

            screenshot = np.array(pyg.screenshot(region=(1632, 290, 10, 727)))
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)

            pyg.click(x_init, y_init)

            low = np.array([50, 100, 100])
            upper = np.array([70, 255, 255])

            pyg.click(x_init, y_init)

            mask = cv2.inRange(screenshot, low, upper)
            coord_white = np.argwhere(mask == 255)

            pyg.click(x_init, y_init)

            if len(coord_white) >= 5:
                buy_x, buy_y = coord_white[0][0], coord_white[0][1]
                # pyg.moveTo(1632+1, 290+79)
                pyg.click(buy_y + 1632, buy_x + 290)

            pyg.click(x_init, y_init)

            if key.is_pressed('e'):
                cv2.destroyAllWindows()
                exit(0)
