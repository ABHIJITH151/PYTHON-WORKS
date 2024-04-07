import pyautogui
import keyboard
import sys
import time
stop = False

def stop_execution():
    global stop
    print("Execution stopped.")
    stop = True

keyboard.add_hotkey('esc', stop_execution)

# Add a delay to allow the hotkey registration to take effect
time.sleep(1)

for i in range(1):
    if stop:
        break
    else:
        pyautogui.press('win')
        pyautogui.sleep(1)
        pyautogui.typewrite('google')
        if stop:
            break
        pyautogui.sleep(1)
        pyautogui.press('enter')
        if stop:
            break
        pyautogui.sleep(2)
        pyautogui.typewrite('https://webmail.mail.dnyan.co.in/')
        pyautogui.press('enter')
        pyautogui.sleep(8)
        pyautogui.typewrite('abhijith.ks@mail.dnyan.co.in')
        pyautogui.press('tab')
        pyautogui.typewrite('Abhijith@111#')
        pyautogui.press('enter')

        if stop:
            break
        pyautogui.press('enter')
