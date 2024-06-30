import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton
import pyautogui
import keyboard
import time
stop = False
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel('Hello, ABHIJITH')
        self.button = QPushButton('Click me')
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setWindowTitle('My PyQt App')
        self.show()
    def on_button_click(self):
        self.label.setText('Button clicked')

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
                if stop:
                    break
                pyautogui.sleep(8)
                pyautogui.typewrite('abhijith.ks@mail.dnyan.co.in')
                pyautogui.press('tab')
                pyautogui.typewrite('Abhijith@111#')
                pyautogui.press('enter')

                if stop:
                    break
                pyautogui.press('enter')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
