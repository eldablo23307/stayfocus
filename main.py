#Importing the main library i will use
import pyautogui
import time
import random

#setup the 2 variable that will the achivement and the browser
object = pyautogui.prompt("What is your achivement?")
browser = pyautogui.prompt("What browser do you usually use?")

#Creating the function that will open the browser
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

#The main loop
while True:

    #Setup the rest time between 5 - 20 minute
    time.sleep(random.randint(300,1200))

    #Checking if the user is working
    check = pyautogui.confirm(f"You are working on {object}", buttons = ["Yes", "No"])

    #Using the date take in the check variable the if statement
    if check != "Yes":

        go_back_to_work(object, browser)

    else:

        pyautogui.alert("Nice job keep going")