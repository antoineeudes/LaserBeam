import sys
import os
import time

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import pyqtSlot, Qt, QEventLoop, QTimer

sys.path.insert(0,'..')
from src.box import Box, generate_random_box
from src.obstacles import ForwardSlashMirror, BackSlashMirror, SquareMirror, HorizontalMirror, VerticalMirror, Transporter

class Button(QPushButton):

    def on_click(self):
        if self.value in self._win.solutions:
            print('Success')
            return True
        print('Incorrect')
        return False

    def __init__(self, x, y, win, text):
        QPushButton.__init__(self, text)
        self._x = x
        self._y = y
        self._win = win
        self.value = None
        self.clicked.connect(self.on_click)


class UpButton(Button):

    def __init__(self, x, y, win):
        Button.__init__(self, x, y, win, '^')
        win.grid.addWidget(self, x+1, y+3)
        self.value = '^' + chr(self._y+65)


class DownButton(Button):

    def __init__(self, x, y, win):
        Button.__init__(self, x, y, win, 'v')
        win.grid.addWidget(self, x+3, y+3)
        self.value = 'v' + chr(self._y+65)

class LeftButton(Button):

    def __init__(self, x, y, win):
        Button.__init__(self, x, y, win, '<')
        win.grid.addWidget(self, x+3, y+1)
        self.value = '<' + chr(self._x+65)

class RightButton(Button):

    def __init__(self, x, y, win):
        Button.__init__(self, x, y, win, '>')
        win.grid.addWidget(self, x+3, y+3)
        self.value = '>' + chr(self._x+65)


class TextArea(QLabel):
    def __init__(self, x, y, text, win):
        self._win = win
        QLabel.__init__(self)
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        win.grid.addWidget(self, x, y)
        win.text_areas[x, y] = self

class Window(QWidget):

    def addInterrogationPoints(self, height, width):
        for i in range(0, height):
            TextArea(i+3, 0, '?', self)
            TextArea(i+3, width+4, '?', self)
        for j in range(0, width):
            TextArea(0, j+3, '?', self)
            TextArea(height+4, j+3, '?', self)

    def addButtons(self, height, width):
        for i in range(0, height):
            LeftButton(i, 0, self)
            RightButton(i, width, self)
        for j in range(0, width):
            UpButton(0, j, self)
            DownButton(height, j, self)

    def displayObstacles(self):
        for i in range(0, self.box.height):
            for j in range(0, self.box.width):
                pic = QLabel(self)
                if isinstance(self.box[j, i], ForwardSlashMirror):
                    pic.setPixmap(QPixmap(os.getcwd() + "/images/forward_slash_mirror.png"))
                elif isinstance(self.box[j, i], BackSlashMirror):
                    pic.setPixmap(QPixmap(os.getcwd() + "/images/back_slash_mirror.png"))
                elif isinstance(self.box[j, i], HorizontalMirror):
                    pic.setPixmap(QPixmap(os.getcwd() + "/images/horizontal_mirror.png"))
                elif isinstance(self.box[j, i], VerticalMirror):
                    pic.setPixmap(QPixmap(os.getcwd() + "/images/vertical_mirror.png"))
                elif isinstance(self.box[j, i], SquareMirror):
                    pic.setPixmap(QPixmap(os.getcwd() + "/images/square_mirror.png"))
                elif isinstance(self.box[j, i], Transporter):
                    pic.setPixmap(QPixmap(os.getcwd() + "/images/Transporter.png"))
                else:
                    pic.setPixmap(QPixmap(os.getcwd() + "/images/aether.png"))
                self.grid.addWidget(pic,i+3,j+3)

    def __init__(self, number_of_cols, number_of_lines):
        self.entry_point = '>A'
        self.text_areas = dict()
        self.box = generate_random_box(number_of_cols, number_of_lines)
        QWidget.__init__(self)
        self.grid = QGridLayout()
        self.displayObstacles()
        self.addInterrogationPoints(self.box.height, self.box.width)
        self.addButtons(self.box.height, self.box.width)
        self.solutions = self.box.find_exits(self.entry_point)
        print(self.solutions)

    def display(self):
        self.setLayout(self.grid)
        self.setWindowTitle("LaserBeam")
        self.show()

    def clear(self):
        for i in range(0, self.box.height):
            for j in range(0, self.box.width):
                pic = QLabel(self)
                pic.setPixmap(QPixmap(os.getcwd() + "/images/aether.png"))
                self.grid.addWidget(pic,i+3,j+3)
        for i in range(0, self.box.height):
            self.text_areas[i+3, 0].setText(' ')
            self.text_areas[i+3, self.box.width+4].setText(' ')
        for j in range(0, self.box.width):
            self.text_areas[0, j+3].setText(' ')
            self.text_areas[self.box.height+4, j+3].setText(' ')
        direction, letter = self.entry_point
        if direction == '>':
            y = 0
        elif direction == '<':
            y = self.box.width+4


if __name__ == '__main__':
    app = QApplication(sys.argv)
    number_of_lines = 7
    number_of_cols = 8

    win = Window(9, 3)
    win.display()
    loop = QEventLoop()
    QTimer.singleShot(5000, loop.quit)
    loop.exec_()
    win.clear()
    win.display()
    sys.exit(app.exec_())
