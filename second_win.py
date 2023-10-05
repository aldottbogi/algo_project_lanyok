from pyQt5.QtCore import Qt
from pyQt5.Qwidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QInputDialoge
from instr import *
class TestWin(QWidget):
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
        self.hello_text = QLabel(txt_title)
        self.input = QInputDialoge(text10)
        self.instruction = QLabel(text2)
        self.input4 = QInputDialoge(text14)
        self.instruction1 = QLabel(text3)
        self.button = QPushButton(buttontext)
        self.input1 = QInputDialoge(text11)
        self.instruction2 = QLabel(text5)
        self.button1 = QPushButton(buttontext2)
        self.instruction3 = QLabel(text6)
        self.button2 = QPushButton(buttontext3)
        self.input2 = QInputDialoge(text12)
        self.input3 = QInputDialoge(text13)
        self.button3 = QPushButton(buttontext4)
        #self.hello_text.addWidget(self.layout)
        #self.instruction.addWidget(self.layout)
        #self.button.addWidget(self.layout)