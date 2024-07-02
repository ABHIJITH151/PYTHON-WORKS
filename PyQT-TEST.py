import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QMessageBox
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt, QTimer
import pyautogui
import keyboard
import threading

stop = False

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Add QLabel for "Have a nice day" with custom font size and style
        self.nice_day_label = QLabel('Hello, ABHIJITH 😊')
        self.nice_day_label.setAlignment(Qt.AlignCenter)
        font = QFont('Arial', 20, QFont.Bold)
        self.nice_day_label.setFont(font)
        self.nice_day_label.setStyleSheet('color: white;')
        layout.addWidget(self.nice_day_label)

        # Set window background color to black using stylesheet
        self.setStyleSheet('background-color: black;')

        # Create horizontal layout for buttons and spacer
        button_layout = QHBoxLayout()

        # Create and configure the buttons
        button_labels = [f'Button {i+1}' for i in range(10)]

        colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300']

        self.buttons = []
        for index, label in enumerate(button_labels):
            button = QPushButton(label)
            button.clicked.connect(self.on_button_click)
            button.setStyleSheet('''
                QPushButton {
                    background-color: %s;
                    color: white;
                    border: none;
                    min-width: 100px;
                    min-height: 60px;
                }
                QPushButton:hover {
                    background-color: %s;
                    border: 2px solid white;
                    border-radius: 5px;
                }
            ''' % (colors[index % len(colors)], QColor(colors[index % len(colors)]).darker().name()))

            button_layout.addWidget(button)  # Add buttons to the horizontal layout
            self.buttons.append(button)

        # Add horizontal layout to main layout
        layout.addLayout(button_layout)

        # Add stretch to push widgets to the top
        layout.addStretch()

        self.setLayout(layout)

        # Show the window maximized
        self.showMaximized()

        self.setWindowTitle('My PyQt App')

    def on_button_click(self):
        button = self.sender()
        self.nice_day_label.setText(f'{button.text()} clicked')

        # Check if the button text matches 'Button 1' for the first button
        if button.text() == 'Button 1':
            self.perform_login()

        # Add conditions for other buttons if needed

    def perform_login(self):
        self.nice_day_label.setText('LOGIN button clicked')

        def stop_execution():
            global stop
            print("Execution stopped.")
            stop = True

        keyboard.add_hotkey('esc', stop_execution)

        # Use threading to avoid blocking the GUI
        thread = threading.Thread(target=self.execute_login)
        thread.start()

    def execute_login(self):
        try:


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
        except Exception as e:
            print(f"An error occurred during login: {e}")
            self.show_error_message("Login Error", f"An error occurred during login: {e}")

    def show_error_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
