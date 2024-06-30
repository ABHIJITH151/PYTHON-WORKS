import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QGridLayout
from PyQt5.QtGui import QFont  # Import QFont for font customization
from PyQt5.QtCore import Qt  # Import Qt for alignment
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

        # Create and configure the label
        self.label = QLabel('Hello, ABHIJITH')
        self.label.setAlignment(Qt.AlignCenter)  # Center align the label horizontally
        self.label.setStyleSheet('color: white;')  # Set text color to white
        layout.addWidget(self.label)

        # Create grid layout for buttons
        grid_layout = QGridLayout()

        # Create and configure the buttons
        button_labels = [f'Button {i+1}' for i in range(50)]

        positions = [(i, j) for i in range(10) for j in range(5)]  # 10 rows, 5 columns for 50 buttons

        self.buttons = []
        colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300',
                  '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300',
                  '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300',
                  '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300',
                  '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300',
                  '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300',
                  '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300',
                  '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300',
                  '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300',
                  '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300']

        for index, label in enumerate(button_labels):
            button = QPushButton(label)
            button.clicked.connect(self.on_button_click)
            if index < len(colors):
                button.setStyleSheet(f'background-color: {colors[index]}; color: white; border: none;')
            else:
                button.setStyleSheet('color: white; border: none;')
            button.setMinimumWidth(200)  # Set minimum width for the buttons
            button.setMinimumHeight(80)  # Set minimum height for the buttons
            grid_layout.addWidget(button, *positions[index])
            self.buttons.append(button)

        # Add grid layout to main layout
        layout.addLayout(grid_layout)

        # Add stretch to push widgets to the top
        layout.addStretch()

        # Add QLabel for "Have a nice day" with custom font size and style
        self.nice_day_label = QLabel('Have a nice day 😊')  # Added a smiley emoji
        self.nice_day_label.setAlignment(Qt.AlignCenter)  # Center align the text horizontally
        font = QFont('Arial', 36, QFont.Bold)  # Example: Arial font, size 36, bold
        self.nice_day_label.setFont(font)
        self.nice_day_label.setStyleSheet('color: white;')  # Set text color to white
        layout.addWidget(self.nice_day_label)

        self.setLayout(layout)

        # Show the window maximized (full-screen mode with taskbar visible)
        self.showMaximized()

        # Set window background color to black using stylesheet
        self.setStyleSheet('background-color: black;')

        self.setWindowTitle('My PyQt App')

    def on_button_click(self):
        button = self.sender()
        self.label.setText(f'{button.text()} clicked')

        # Check if the button text matches 'Button 1' for the first button
        if button.text() == 'Button 1':
            self.perform_login()

        # Add conditions for other buttons if needed

    def perform_login(self):
        self.label.setText('LOGIN button clicked')

        def stop_execution():
            global stop  # Use global instead of nonlocal for a global variable
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
