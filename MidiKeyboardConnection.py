def midi_keyboard_connection(self):
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

    self.cl_button.loop = False
    self.cl1_button.loop = False
    self.dl_button.loop = False
    self.dl1_button.loop = False
    self.el_button.loop = False
    self.fl_button.loop = False
    self.fl1_button.loop = False
    self.gl_button.loop = False
    self.gl1_button.loop = False
    self.al_button.loop = False
    self.al1_button.loop = False
    self.hl_button.loop = False

    self.ch_button.loop = False
    self.ch1_button.loop = False
    self.dh_button.loop = False
    self.dh1_button.loop = False
    self.eh_button.loop = False
    self.fh_button.loop = False
    self.fh1_button.loop = False
    self.gh_button.loop = False
    self.gh1_button.loop = False
    self.ah_button.loop = False
    self.ah1_button.loop = False
    self.hh_button.loop = False