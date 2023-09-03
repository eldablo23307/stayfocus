import pyautogui
import time
import random

object = pyautogui.prompt("What is your achivement?")
browser = pyautogui.prompt("What browser do you usually use?")

run = True

def go_back_to_work(x, y):
    pyautogui.press("win")
    time.sleep(0.2)
    pyautogui.typewrite(y)
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "t")
    time.sleep(5)
    pyautogui.typewrite(x)
    time.sleep(0.2)
    pyautogui.press("enter")

while run:

    time.sleep(random.randint(300,1200))

    check = pyautogui.confirm(f"You are working on {object}", buttons = ["Yes", "No"])

    if check != "Yes":

        go_back_to_work(object, browser)
    else:

        pyautogui.alert("Nice job keep going")