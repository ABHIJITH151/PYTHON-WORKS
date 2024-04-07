import pyautogui
pyautogui.sleep(1)
screen_width, screen_height = pyautogui.size()
print(f"Screen Resolution: {screen_width} x {screen_height}")
pyautogui.sleep(5)
mouse_x, mouse_y = pyautogui.position()
print(f"Mouse Coordinates: {mouse_x} x {mouse_y}")