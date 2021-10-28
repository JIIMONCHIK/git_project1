import sys
import sqlite3
import PyQt5
import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from First import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cl_button.pressed.connect(self.run)
        self.cl1_button.pressed.connect(self.run)
        self.dl_button.pressed.connect(self.run)
        self.dl1_button.pressed.connect(self.run)
        self.el_button.pressed.connect(self.run)
        self.fl_button.pressed.connect(self.run)
        self.fl1_button.pressed.connect(self.run)
        self.gl_button.pressed.connect(self.run)
        self.gl1_button.pressed.connect(self.run)
        self.al_button.pressed.connect(self.run)
        self.al1_button.pressed.connect(self.run)
        self.hl_button.pressed.connect(self.run)

        self.ch_button.pressed.connect(self.run)
        self.ch1_button.pressed.connect(self.run)
        self.dh_button.pressed.connect(self.run)
        self.dh1_button.pressed.connect(self.run)
        self.eh_button.pressed.connect(self.run)
        self.fh_button.pressed.connect(self.run)
        self.fh1_button.pressed.connect(self.run)
        self.gh_button.pressed.connect(self.run)
        self.gh1_button.pressed.connect(self.run)
        self.ah_button.pressed.connect(self.run)
        self.ah1_button.pressed.connect(self.run)
        self.hh_button.pressed.connect(self.run)

        self.cl_button.released.connect(self.rel)
        self.cl1_button.released.connect(self.rel)
        self.dl_button.released.connect(self.rel)
        self.dl1_button.released.connect(self.rel)
        self.el_button.released.connect(self.rel)
        self.fl_button.released.connect(self.rel)
        self.fl1_button.released.connect(self.rel)
        self.gl_button.released.connect(self.rel)
        self.gl1_button.released.connect(self.rel)
        self.al_button.released.connect(self.rel)
        self.al1_button.released.connect(self.rel)
        self.hl_button.released.connect(self.rel)

        self.ch_button.released.connect(self.rel)
        self.ch1_button.released.connect(self.rel)
        self.dh_button.released.connect(self.rel)
        self.dh1_button.released.connect(self.rel)
        self.eh_button.released.connect(self.rel)
        self.fh_button.released.connect(self.rel)
        self.fh1_button.released.connect(self.rel)
        self.gh_button.released.connect(self.rel)
        self.gh1_button.released.connect(self.rel)
        self.ah_button.released.connect(self.rel)
        self.ah1_button.released.connect(self.rel)
        self.hh_button.released.connect(self.rel)

    def run(self):
        print(self.sender().text())
        self.sender().time = datetime.datetime.now()

    def rel(self):
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