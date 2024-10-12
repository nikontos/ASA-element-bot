from datetime import datetime, timedelta
import time
import pyautogui
import requests
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image

gp_cord = {"x": 1602, "y": 285}


def get_cords():
    time.sleep(2)
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX, currentMouseY)


def craft_gp():
    pyautogui.moveTo(gp_cord["x"], gp_cord["y"], duration=0.5)
    pyautogui.click()
    # pyautogui.keyDown("a")
    pyautogui.press("a")
    pyautogui.press("a")
    pyautogui.press("a")
    pyautogui.press("a")
    pyautogui.press("a")
    pyautogui.press("a")
    pyautogui.press("a")
    pyautogui.press("a")
    pyautogui.press("a")
    pyautogui.press("a")
    pyautogui.press("a")

    pyautogui.press("f")

    # pyautogui.keyDown("a")
    # time.sleep(0.2)
    # pyautogui.keyUp("a")
    # pyautogui.keyUp("a")


def move_to_next_chemb():
    time.sleep(0.1)
    pyautogui.keyDown("a")
    time.sleep(0.225)
    pyautogui.keyUp("a")
    time.sleep(1)
    pyautogui.press("f")


def main(current, total):
    while current < total:
        move_to_next_chemb()
        time.sleep(0.5)
        craft_gp()
        current += 1


# get_cords()
main(0, 7)
