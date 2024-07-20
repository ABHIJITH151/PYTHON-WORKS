import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox,
                             QRadioButton, QLineEdit)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
import threading
import pyautogui
import keyboard

stop = False

class SignalScaler(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Signal Type Selection
        self.radio0_20 = QRadioButton("0-20mA")
        self.radio4_20 = QRadioButton("4-20mA")
        self.radio0_20.setChecked(True)

        layout.addWidget(QLabel("SIGNAL TYPE"))
        layout.addWidget(self.radio0_20)
        layout.addWidget(self.radio4_20)

        # Input for Y1 and Y2
        layout.addWidget(QLabel("BOTTOM SCALE (Y1)"))
        self.inputY1 = QLineEdit()
        layout.addWidget(self.inputY1)

        layout.addWidget(QLabel("TOP SCALE (Y2)"))
        self.inputY2 = QLineEdit()
        layout.addWidget(self.inputY2)

        # Input for X (current value)
        layout.addWidget(QLabel("Input Current Value (mA)"))
        self.inputX = QLineEdit()
        self.inputX.textChanged.connect(self.updateScaledValue)
        layout.addWidget(self.inputX)

        # Scaled Value Input
        layout.addWidget(QLabel("Scaled Value (Y)"))
        self.inputY = QLineEdit()
        self.inputY.textChanged.connect(self.updateCurrentValue)
        layout.addWidget(self.inputY)

        # Calculate Button
        self.calculateBtn = QPushButton("Calculate")
        self.calculateBtn.clicked.connect(self.calculateScaledValue)
        layout.addWidget(self.calculateBtn)

        self.setLayout(layout)
        self.setStyleSheet('background-color: white; color: black;')

    def calculateScaledValue(self):
        X1, X2 = (0, 20) if self.radio0_20.isChecked() else (4, 20)
        try:
            Y1 = float(self.inputY1.text())
            Y2 = float(self.inputY2.text())
            X = float(self.inputX.text())
            Y = ((X - X1) * (Y2 - Y1) / (X2 - X1)) + Y1
            self.inputY.setText(f"{Y:.2f}")
        except ValueError:
            self.inputY.setText("Invalid input")
        except ZeroDivisionError:
            self.inputY.setText("Division by zero")

    def updateScaledValue(self):
        X1, X2 = (0, 20) if self.radio0_20.isChecked() else (4, 20)
        try:
            Y1 = float(self.inputY1.text())
            Y2 = float(self.inputY2.text())
            X = float(self.inputX.text())
            Y = ((X - X1) * (Y2 - Y1) / (X2 - X1)) + Y1
            self.inputY.setText(f"{Y:.2f}")
        except ValueError:
            pass

    def updateCurrentValue(self):
        X1, X2 = (0, 20) if self.radio0_20.isChecked() else (4, 20)
        try:
            Y1 = float(self.inputY1.text())
            Y2 = float(self.inputY2.text())
            Y = float(self.inputY.text())
            X = ((Y - Y1) * (X2 - X1) / (Y2 - Y1)) + X1
            self.inputX.setText(f"{X:.2f}")
        except ValueError:
            pass

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.stack = QWidget()
        self.stack_layout = QVBoxLayout()

        # Add QLabel for "Hello, ABHIJITH 😊" with custom font size and style
        self.nice_day_label = QLabel('Hello, ABHIJITH 😊')
        self.nice_day_label.setAlignment(Qt.AlignCenter)
        font = QFont('Arial', 20, QFont.Bold)
        self.nice_day_label.setFont(font)
        self.nice_day_label.setStyleSheet('color: white;')
        self.stack_layout.addWidget(self.nice_day_label)

        # Set window background color to black using stylesheet
        self.stack.setStyleSheet('background-color: black;')

        # Create horizontal layout for buttons and spacer
        button_layout = QHBoxLayout()

        # Create and configure the buttons
        button_labels = ['Button 1', 'Button 2']
        colors = ['#FF5733', '#C70039']

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
            ''' % (colors[index], QColor(colors[index]).darker().name()))

            button_layout.addWidget(button)  # Add buttons to the horizontal layout
            self.buttons.append(button)

        self.stack_layout.addLayout(button_layout)
        self.stack_layout.addStretch()

        self.stack.setLayout(self.stack_layout)

        # Show the window maximized
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.stack)
        self.showMaximized()

        self.setWindowTitle('My PyQt App')

    def on_button_click(self):
        button = self.sender()
        if button.text() == 'Button 1':
            self.perform_login()
        elif button.text() == 'Button 2':
            self.show_signal_scaler_popup()

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

    def show_signal_scaler_popup(self):
        self.signal_scaler_popup = QWidget()
        self.signal_scaler_popup.setWindowTitle("Signal Scaler")
        self.signal_scaler_popup.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        # Add SignalScaler widget to popup
        self.signal_scaler = SignalScaler()
        layout.addWidget(self.signal_scaler)

        self.signal_scaler_popup.setLayout(layout)
        self.signal_scaler_popup.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
