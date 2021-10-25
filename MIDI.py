import sys
import sqlite3
import PyQt5

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from First import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.run)
        self.pushButton_4.clicked.connect(self.run)
        self.pushButton_5.clicked.connect(self.run)
        self.pushButton_6.clicked.connect(self.run)
        self.pushButton_7.clicked.connect(self.run)

    def run(self):
        print(self.sender().text())
        self.sender().test


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())