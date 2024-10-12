from datetime import datetime, timedelta
import time
import pyautogui
import requests
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image

# 41m41s for 1 node recharging
current_node = 0
total_nodes = 62
skiped = 5
total_nodes = 39
# total_nodes = total_nodes - skiped
recon_counter = {}
ele_icon = {"x": 1234, "y": 283}
search_bar = {"x": 1279, "y": 200}
element_cords = {"x": 1335, "y": 268}
new_ele = {"x": 1335, "y": 277}


def msg_discord(message):
    url = "https://discord.com/api/webhooks/1284196153637994547/EpxEC7q3nAPm82qA7A1SClOxVuY0jBgMAKpOrsflAkO6AxJQ_WsyQ8xcZGwbE0k-QENv"
    msg = {"content": message}
    requests.post(url, json=msg)


def post_screenshot_to_discord():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    url = "https://discord.com/api/webhooks/1284196153637994547/EpxEC7q3nAPm82qA7A1SClOxVuY0jBgMAKpOrsflAkO6AxJQ_WsyQ8xcZGwbE0k-QENv"
    with open("screenshot.png", "rb") as f:
        requests.post(url, files={"file": f})


def teleport_to_next():
    pyautogui.keyDown("down")
    time.sleep(3)
    pyautogui.keyUp("down")
    time.sleep(1)
    pyautogui.press("r")


def craft_element(reconnected=False, retries=0):
    if retries >= 3:
        msg_discord("Max retries exceeded, continuing")
        post_screenshot_to_discord()
        return
        # if not reconnected:
        # pyautogui.keyDown("d")
        # time.sleep(0.5)
        # pyautogui.keyUp("d")
        # time.sleep(0.5)
        # pyautofef`reconnect
        # awef`reconnect
        # awgf`reconnect
        # ui.ff`reconnecttff`reconnecttftf
        # aw`ferrr
        # awefekeyDowffffffff`recornnectff`reconnecttftf
        # awefetftfrr
        # awefeeeeeeen("w")tftftftftftftftfrr
        # time.sleep(1.5)rrrrrrrr
        # pyautogui.keyUp("W")

    if reconnected:
        pyautogui.keyDown("a")
        time.sleep(1)
        pyautogui.keyUp("a")
        time.sleep(0.5)
        pyautogui.keyDown("w")
        time.sleep(1)
        pyautogui.keyUp("W")
        time.sleep(0.3)
        pyautogui.press("right")
        pyautogui.keyDown("d")
        time.sleep(0.1)
        pyautogui.keyUp("d")

    if not reconnected:
        time.sleep(2)
        pyautogui.keyDown("up")
        time.sleep(0.4)
        pyautogui.keyUp("up")

    time.sleep(1)
    pyautogui.press("f")
    time.sleep(2)  # lel laged when i opened inv and got false reconnect
    opened_inv = screenshot_and_compare("inventory.png")
    if not opened_inv:
        retries += 1
        print("Gotta reconnect")
        msg_discord("```I bugged -- reconnecting :( ```")
        reconnect()
        craft_element(True, retries)
        return

    pyautogui.moveTo(ele_icon["x"], ele_icon["y"], duration=0.5)
    pyautogui.press("e")


def collect_element():
    # pyautogui.moveTo(search_bar["x"], search_bar["y"], duration=0.5)
    # time.sleep(2)
    # pyautogui.click()
    # time.sleep(0.5)
    # pyautogui.write("element")
    # time.sleep(1)
    pyautogui.moveTo(new_ele["x"], new_ele["y"], duration=0.3)
    time.sleep(1)
    pyautogui.click()
    pyautogui.press("t")
    time.sleep(1)
    put_bat_back()
    pyautogui.press("f")


def reconnect(repeats=1):
    # recon_counter.update(current_node, current_node + 1)
    pyautogui.press("`")
    time.sleep(1)
    pyautogui.write("reconnect")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(80)


def put_bat_back():
    # pyautogui.moveTo(265, 196, duration=0.5)
    # time.sleep(0.2)
    # pyautogui.click()
    # time.sleep(0.5)
    # pyautogui.write("bat")
    # time.sleep(1)
    pyautogui.moveTo(355, 209, duration=0.5)
    time.sleep(0.2)
    pyautogui.click()


def move_back_to_tp():
    pyautogui.keyDown("s")
    time.sleep(0.3)
    pyautogui.keyUp("s")


def drink_water():
    time.sleep(0.5)
    pyautogui.press("2")
    time.sleep(0.5)
    pyautogui.press("3")


def helping_stuff():
    # Move mouse to (x, y) coordinates on the screen
    pyautogui.moveTo(100, 100)

    # Click the left mouse button
    pyautogui.click()

    # Right-click
    pyautogui.rightClick()

    # Double-click
    pyautogui.doubleClick()

    # Move mouse to (x, y) and drag to another position while holding down left click
    pyautogui.moveTo(500, 500, duration=1)

    # Type out a string
    pyautogui.write("Hello, world!")

    # Press a single key
    pyautogui.press("enter")

    # Press a combination of keys (e.g., Ctrl+C for copy)
    pyautogui.hotkey("ctrl", "c")

    # Press and hold a key, then release
    pyautogui.keyDown("shift")
    pyautogui.press("a")
    pyautogui.keyUp("shift")

    # Get screen size
    width, height = pyautogui.size()

    # Get current mouse position
    currentMouseX, currentMouseY = pyautogui.position()


def donate_element():
    time.sleep(7)
    pyautogui.keyDown("up")
    time.sleep(0.7)
    pyautogui.keyUp("up")
    time.sleep(3)
    pyautogui.press("e")
    time.sleep(0.3)
    post_screenshot_to_discord()


def get_cords():
    time.sleep(2)
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX, currentMouseY)


def take_screenshot():
    # Take a screenshot using pyautogui and convert it to OpenCV format
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot


def load_saved_screenshot(filepath):
    # Load the saved screenshot using OpenCV
    saved_screenshot = cv2.imread(filepath)
    return saved_screenshot


def compare_images(image1, image2, threshold=0.9):
    # Resize the images to be the same size for comparison
    image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculate the Structural Similarity Index (SSIM) between the images
    similarity_index, _ = ssim(gray1, gray2, full=True)

    print(f"Similarity index: {similarity_index}")

    # Check if the similarity index meets the threshold
    return similarity_index >= threshold


def screenshot_and_compare(saved_screenshot_path, threshold=0.49):
    # Take a new screenshot
    new_screenshot = take_screenshot()

    # Load the saved screenshot
    saved_screenshot = load_saved_screenshot(saved_screenshot_path)

    # Compare the screenshots
    if compare_images(new_screenshot, saved_screenshot, threshold):
        print("Images are similar enough.")
        return True
    else:
        print("Images are not similar.")
        return False


def main():
    global current_node, total_nodes
    print(recon_counter)
    msg_discord("```Bot Started```")

    next_drink_time = datetime.now() + timedelta(minutes=24)

    while True:
        try:
            current_node += 1
            if current_node > total_nodes:
                time.sleep(1)
                teleport_to_next()
                time.sleep(1)
                donate_element()
                current_node = 1
                msg_discord("*Going to sleep for 5m*  :sleeping: ")
                time.sleep(300)  # 12m sleep, my timer was 10m
                msg_discord("```Starting new cycle```")
            time.sleep(2)
            teleport_to_next()
            msg_discord(f"I am at node {current_node}")
            time.sleep(2)  # time to render after tp to next node
            craft_element()
            # sleep until ele is crafted
            time.sleep(33)
            collect_element()
            time.sleep(1)
            # move_back_to_tp()
            current_time = datetime.now()
            if current_time > next_drink_time:
                drink_water()
                next_drink_time = current_time + timedelta(minutes=48)
        except Exception as e:
            msg_discord(f"Error: {e}")
            continue


main()
# time.sleep(2)
# post_screenshot_to_discord()
# drink_water()
# time.sleep(1.3)
# teleport_to_next()
# time.sleep(1.5)
# craft_element()
# time.sleep(1)
# move_back_to_tp()
# donate_element()
# get_cords()
# time.sleep(3)
# reconnect()
# time.sleep(1)
# screenshot_and_compare("inventory.png")
