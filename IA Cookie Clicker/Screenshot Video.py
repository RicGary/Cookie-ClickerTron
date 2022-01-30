import pyautogui as pyg
from Init_Big_Cookie import InitCoordsBigCookie
import keyboard as key
import numpy as np
import cv2
import time

"""
Tela = pyg.screenshot()
Tela = np.array(Tela)
Tela = cv2.cvtColor(Tela, cv2.COLOR_RGB2BGR)
"""

metodo = cv2.TM_CCOEFF_NORMED
template = cv2.imread('Imagens/BuyCursor.JPG', 0)
h, w = template.shape

while True:

    screenshot = pyg.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    resultado = cv2.matchTemplate(screenshot, template, metodo)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    y, x = max_loc
    inf_dir = (w + y, h + x)

    cv2.rectangle(screenshot, max_loc, inf_dir, 255, 5)

    cv2.imshow('Screen Recorder', screenshot)
    cv2.waitKey(0)
    """if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break"""

