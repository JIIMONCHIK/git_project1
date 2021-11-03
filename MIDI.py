import sys
import sqlite3
import datetime

from MidiKeyboardConnection import *
from KeySoundConnection import *
from ComputerKeyboardConnection import *
from ChooseSound import *
from DatabaseCreation import *
from ToolKeysConnection import *
from DatabaseShow import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from First import Ui_MainWindow


class MIDI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        choose_sound(self)
        self.pause = 0
        self.seq = []
        self.rec = False
        self.start_playing = False
        tool_keys_connetion(self)   # подключение служебных кнопок
        midi_keyboard_connection(self)  # подключение кнопок MIDI
        key_sound_connection(self, self.path, self.format)
        computer_keyboard_control(self)
        self.player = QtMultimedia.QMediaPlayer()

    def run(self, note=False):
        if self.start_playing:
            pause_time = datetime.datetime.now() - self.pause
            self.seq.append(('Pause', pause_time.total_seconds()))
        if not note:
            note = self.sender()
        note.time = datetime.datetime.now()
        self.player.setMedia(note.tone)
        self.player.play()

    def rel(self, note=False):
        if not self.start_playing:
            self.start_playing = True
        self.pause = datetime.datetime.now()
        if not note:
            note = self.sender()
        press_time = datetime.datetime.now() - note.time
        self.seq.append((note.text(), press_time.total_seconds()))
        self.player.stop()

    def change_sound(self):
        choose_sound(self)
        key_sound_connection(self, self.path, self.format)

    # def keyPressEvent(self, event):
    #     keyboard_pressed(self, event)

    def record(self):
        if self.rec:
            name = self.choose_name()
            if name:
                database_creation(name)
                for i in range(len(self.seq)):
                    database_insert(name, self.seq[i])
                show_database(self, name)
        else:
            self.seq = []
            self.start_playing = False
            self.rec = True

    def choose_name(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите имя файла",
                                                'Введите желаемое имя файла')
        if ok_pressed:
            return name + '.db'
        return False

    # def keyReleaseEvent(self, event):
    #     keyboard_released(self, event)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MIDI()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())