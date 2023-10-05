from pyQt5.QtCore import Qt
from pyQt5.Qwidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apper()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self): 
        self.hello_text = QLabel(text7)
        self.instruction = QLabel(text8)

