from PyQt5 import QtCore, QtMultimedia


def key_sound_connection(self, path, format):
    self.cl_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Cl' + format))
    self.cl1_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Cl1' + format))
    self.dl_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Dl' + format))
    self.dl1_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Dl1' + format))
    self.el_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/El' + format))
    self.fl_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Fl' + format))
    self.fl1_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Fl1' + format))
    self.gl_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Gl' + format))
    self.gl1_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Gl1' + format))
    self.al_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Al' + format))
    self.al1_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Al1' + format))
    self.hl_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Hl' + format))

    self.ch_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Ch' + format))
    self.ch1_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Ch1' + format))
    self.dh_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Dh' + format))
    self.dh1_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Dh1' + format))
    self.eh_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Eh' + format))
    self.fh_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Fh' + format))
    self.fh1_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Fh1' + format))
    self.gh_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Gh' + format))
    self.gh1_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Gh1' + format))
    self.ah_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Ah' + format))
    self.ah1_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Ah1' + format))
    self.hh_button.tone = QtMultimedia.\
        QMediaContent(QtCore.QUrl.fromLocalFile(path + '/Hh' + format))

