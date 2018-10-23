import sys
import os

# from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import pyqtSlot, Qt

sys.path.insert(0,'..')
from src.box import *


number_of_lines = 7
number_of_cols = 8
elements = [(0, 0, ForwardSlashMirror()), (1, 0, BackSlashMirror()), (0, 1, HorizontalMirror()), (1, 1, SquareMirror()), (2, 0, Transporter([])), (2, 1, VerticalMirror())]
box = Box(number_of_cols, number_of_lines, elements)
print(box)

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    for i in range(0, number_of_lines):
        for j in range(0, number_of_cols):
            pic = QLabel(win)
            if isinstance(box[j, i], ForwardSlashMirror):
                pic.setPixmap(QPixmap(os.getcwd() + "/images/forward_slash_mirror.png"))
            elif isinstance(box[j, i], BackSlashMirror):
                pic.setPixmap(QPixmap(os.getcwd() + "/images/back_slash_mirror.png"))
            elif isinstance(box[j, i], HorizontalMirror):
                pic.setPixmap(QPixmap(os.getcwd() + "/images/horizontal_mirror.png"))
            elif isinstance(box[j, i], VerticalMirror):
                pic.setPixmap(QPixmap(os.getcwd() + "/images/vertical_mirror.png"))
            elif isinstance(box[j, i], SquareMirror):
                pic.setPixmap(QPixmap(os.getcwd() + "/images/square_mirror.png"))
            elif isinstance(box[j, i], Transporter):
                pic.setPixmap(QPixmap(os.getcwd() + "/images/Transporter.png"))
            else:
                pic.setPixmap(QPixmap(os.getcwd() + "/images/aether.png"))
            grid.addWidget(pic,i+3,j+3)

    for i in range(0, number_of_lines):
        text_left = QLabel()
        text_right = QLabel()
        text_left.setText("?")
        text_right.setText("?")
        grid.addWidget(text_left, i+3, 0)
        grid.addWidget(text_right, i+3, number_of_cols+4)
        button_left = QPushButton('<')
        button_left.setToolTip('This is an example button')
        grid.addWidget(button_left,i+3,1)
        button_right = QPushButton('>')
        button_right.setToolTip('This is an example button')
        grid.addWidget(button_right,i+3,number_of_cols+3)

    for j in range(0, number_of_cols):
        text_up = QLabel()
        text_down = QLabel()
        text_up.setText("?")
        text_down.setText("?")
        text_up.setAlignment(Qt.AlignCenter)
        text_down.setAlignment(Qt.AlignCenter)
        grid.addWidget(text_up, 0, j+3)
        grid.addWidget(text_down, number_of_lines+4, j+3)
        button_up = QPushButton('^')
        button_up.setToolTip('This is an example button')
        grid.addWidget(button_up, 1, j+3)
        button_down = QPushButton('v')
        button_down.setToolTip('This is an example button')
        grid.addWidget(button_down, number_of_lines+3, j+3)


    win.setLayout(grid)
    win.setWindowTitle("LaserBeam")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
