import sys
import sqlite3
import PyQt5
import datetime

from MidiKeyboardConnection import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from First import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pause = 0
        self.start_playing = False
        midi_keyboard_connection(self)  # подключение кнопок MIDI

    def run(self):  # функция
        if self.start_playing:
            pause_time = datetime.datetime.now() - self.pause
            print('pause', pause_time.total_seconds())
        print(self.sender().text())
        self.sender().time = datetime.datetime.now()

    def rel(self):
        if not self.start_playing:
            self.start_playing = True
        self.pause = datetime.datetime.now()
        press_time = datetime.datetime.now() - self.sender().time
        print(press_time.total_seconds())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())