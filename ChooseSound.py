from PyQt5.QtWidgets import QFileDialog


def choose_sound(self):
    self.fPath = QFileDialog.getOpenFileName(self, 'Выбрать файл', './')[0]
    if self.fPath:
        self.path = '/'.join(self.fPath.split('/')[:-1])
        self.format = '.' + self.fPath.split('.')[-1]