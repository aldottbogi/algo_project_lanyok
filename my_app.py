from pyQt5.QtCore import Qt
from pyQt5.Qwidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import *

app = QApplication([])
main_win = QWidget
main_win.show()
app.exec_()

txt_title = "Health"
win_x, win_y = 200, 100
win_width, win_height = 1000, 600

class MainWin(QWidget):
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
        self.hello_text = QLabel(text1)
        self.instruction = QLabel(text22)
        self.button = QPushButton(txt_button)
        self.layout = QVBoxLayout()
        self.hello_text.addWidget(self.layout)
        self.instruction.addWidget(self.layout)
        self.button.addWidget(self.layout)

    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()
        