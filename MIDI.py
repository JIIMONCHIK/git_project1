import sys
import sqlite3
import PyQt5
import datetime

from MidiKeyboardConnection import *
from KeySoundConnection import *
from ComputerKeyboardConnection import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from First import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path = 'C:/Piano'
        self.format = '.m4a'
        self.pause = 0
        self.start_playing = False
        midi_keyboard_connection(self)  # подключение кнопок MIDI
        key_sound_connection(self, self.path, self.format)
        self.player = QtMultimedia.QMediaPlayer()

    def run(self):
        print(self.sender())
        if self.start_playing:
            pause_time = datetime.datetime.now() - self.pause
            print('pause', pause_time.total_seconds())
        self.sender().time = datetime.datetime.now()
        self.player.setMedia(self.sender().tone)
        self.player.play()

    def rel(self):
        if not self.start_playing:
            self.start_playing = True
        self.pause = datetime.datetime.now()
        press_time = datetime.datetime.now() - self.sender().time
        print(press_time.total_seconds())
        self.player.stop()

    def keyPressEvent(self, event):
        keyboard_pressed(self, event)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())