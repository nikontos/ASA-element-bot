from datetime import datetime, timedelta
import time
import pyautogui
import requests
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssimad
from PIL import Image

while True:
    time.sleep(1200)
    # time.sleep(1.4)
    pyautogui.keyDown("a")
    time.sleep(0.1)
    pyautogui.keyUp("a")
    pyautogui.keyDown("d")
    time.sleep(0.1)
    pyautogui.keyUp("d")
