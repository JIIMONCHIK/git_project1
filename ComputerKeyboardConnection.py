from PyQt5.QtCore import Qt


def keyboard_pressed(self, event):
    if event.key() == Qt.Key_Q:
        self.cl_button.pressEvent()
    if event.key() == Qt.Key_W:
        print(2)
        self.cl1_button.pressed()
    if event.key() == Qt.Key_E:
        self.dl_button.pressed()
    if event.key() == Qt.Key_R:
        self.dl1_button.pressed()
    if event.key() == Qt.Key_T:
        self.el_button.pressed()
    if event.key() == Qt.Key_Y:
        self.fl_button.pressed()
    if event.key() == Qt.Key_U:
        self.fl1_button.pressed()
    if event.key() == Qt.Key_I:
        self.gl_button.pressed()
    if event.key() == Qt.Key_O:
        self.gl1_button.pressed()
    if event.key() == Qt.Key_P:
        self.al_button.pressed()
    if event.key() == Qt.Key_BracketLeft:
        self.al1_button.pressed()
    if event.key() == Qt.Key_BracketRight:
        self.hl_button.pressed()

    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()
    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()
    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()
    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()
    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()
    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()
    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()
    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()
    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()
    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()
    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()
    # if event.key() == Qt.Key_Q:
    #     self.cl_button.pressed()