from PyQt5.QtCore import Qt


def computer_keyboard_control(self):
    self.q_released = True
    self.w_released = True
    self.e_released = True
    self.r_released = True
    self.t_released = True
    self.y_released = True
    self.u_released = True
    self.i_released = True
    self.o_released = True
    self.p_released = True
    self.bracketleft_released = True
    self.bracketright_released = True


def keyboard_pressed(self, event):
    if event.key() == Qt.Key_Q:
        if self.q_released:
            self.q_released = False
            self.run(self.cl_button)
            self.q_released = True
    if event.key() == Qt.Key_W:
        if self.w_released:
            self.run(self.cl1_button)
            self.w_released = False
    if event.key() == Qt.Key_E:
        if self.e_released:
            self.run(self.dl_button)
            self.e_released = False
    if event.key() == Qt.Key_R:
        if self.r_released:
            self.run(self.dl1_button)
            self.r_released = False
    if event.key() == Qt.Key_T:
        if self.t_released:
            self.run(self.el_button)
            self.t_released = False
    if event.key() == Qt.Key_Y:
        if self.y_released:
            self.run(self.fl_button)
            self.y_released = False
    if event.key() == Qt.Key_U:
        if self.u_released:
            self.run(self.fl1_button)
            self.u_released = False
    if event.key() == Qt.Key_I:
        if self.i_released:
            self.run(self.gl_button)
            self.i_released = False
    if event.key() == Qt.Key_O:
        if self.o_released:
            self.run(self.gl1_button)
            self.o_released = False
    if event.key() == Qt.Key_P:
        if self.p_released:
            self.run(self.al_button)
            self.p_released = False
    if event.key() == Qt.Key_BracketLeft:
        if self.bracketleft_released:
            self.run(self.al_button)
            self.bracketleft_released = False
    if event.key() == Qt.Key_BracketRight:
        if self.bracketright_released:
            self.run(self.hl_button)
            self.bracketright_released = False


# def keyboard_released(self, event):
#     if event.key() == Qt.Key_Q:
#         if not self.q_released:
#             print(1)
#             self.q_released = True
#             self.rel(self.cl_button)
#     if event.key() == Qt.Key_W:
#         self.w_released = True
#         self.rel(self.cl1_button)
#     if event.key() == Qt.Key_E:
#         self.e_released = True
#         self.rel(self.dl_button)
#     if event.key() == Qt.Key_R:
#         self.r_released = True
#         self.rel(self.dl1_button)
#     if event.key() == Qt.Key_T:
#         self.t_released = True
#         self.rel(self.el_button)
#     if event.key() == Qt.Key_Y:
#         self.y_released = True
#         self.rel(self.fl_button)
#     if event.key() == Qt.Key_U:
#         self.u_released = True
#         self.rel(self.fl1_button)
#     if event.key() == Qt.Key_I:
#         self.i_released = True
#         self.rel(self.gl_button)
#     if event.key() == Qt.Key_O:
#         self.o_released = True
#         self.rel(self.gl1_button)
#     if event.key() == Qt.Key_P:
#         self.p_released = True
#         self.rel(self.al_button)
#     if event.key() == Qt.Key_BracketLeft:
#         self.bracketleft_released = True
#         self.rel(self.al1_button)
#     if event.key() == Qt.Key_BracketRight:
#         self.bracketright_released = True
#         self.rel(self.hl_button)
