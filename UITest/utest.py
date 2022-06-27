import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import untitled


def computer():
    print("cmd")
    os.system("start explorer.exe")


def settings():
    os.system("start 'ms-settings:about'")


def notepad():
    os.system("start notepad.exe")


def cmd():
    os.system("start cmd.exe")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = untitled.Ui_MainWindow()
    ui.pushButton.clicked.connect(computer)
    ui.pushButton_2.clicked.connect(settings)
    ui.pushButton_3.clicked.connect(cmd)
    ui.pushButton_4.clicked.connect(notepad)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
