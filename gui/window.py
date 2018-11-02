# /gui/window.py
import os
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QEventLoop, QTimer
sys.path.insert(0,'..')
from src.box import Box, generate_random_box, int_to_letter, letter_to_int, random_entry_point
from src.obstacles import ForwardSlashMirror, BackSlashMirror, SquareMirror, HorizontalMirror, VerticalMirror, Transporter


class Button(QPushButton):

    def on_click(self):
        if self.value in self._win.solutions:
            return QMessageBox.about(self, "Success", "Well Done! That's a correct exit.")
        return QMessageBox.about(self, "You failed", "Try again!")

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
        self.value = '^' + int_to_letter[self._y]


class DownButton(Button):

    def __init__(self, x, y, win):
        Button.__init__(self, x, y, win, 'v')
        win.grid.addWidget(self, x+3, y+3)
        self.value = 'v' + int_to_letter[self._y]

class LeftButton(Button):

    def __init__(self, x, y, win):
        Button.__init__(self, x, y, win, '<')
        win.grid.addWidget(self, x+3, y+1)
        self.value = '<' + int_to_letter[self._x]

class RightButton(Button):

    def __init__(self, x, y, win):
        Button.__init__(self, x, y, win, '>')
        win.grid.addWidget(self, x+3, y+3)
        self.value = '>' + int_to_letter[self._x]


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

    def addObstacle(self, i, j):
        pic = QLabel(self)
        if isinstance(self.box[j, i], ForwardSlashMirror):
            pic.setPixmap(QPixmap(os.getcwd() + "/gui/images/forward_slash_mirror.png"))
        elif isinstance(self.box[j, i], BackSlashMirror):
            pic.setPixmap(QPixmap(os.getcwd() + "/gui/images/back_slash_mirror.png"))
        elif isinstance(self.box[j, i], HorizontalMirror):
            pic.setPixmap(QPixmap(os.getcwd() + "/gui/images/horizontal_mirror.png"))
        elif isinstance(self.box[j, i], VerticalMirror):
            pic.setPixmap(QPixmap(os.getcwd() + "/gui/images/vertical_mirror.png"))
        elif isinstance(self.box[j, i], SquareMirror):
            pic.setPixmap(QPixmap(os.getcwd() + "/gui/images/square_mirror.png"))
        elif isinstance(self.box[j, i], Transporter):
            pic.setPixmap(QPixmap(os.getcwd() + "/gui/images/Transporter.png"))
        else:
            pic.setPixmap(QPixmap(os.getcwd() + "/gui/images/aether.png"))
        self.grid.addWidget(pic, i+3, j+3)
        self.obstacles_label[i,j] = pic

    def displayObstacles(self):
        for i in range(0, self.box.height):
            for j in range(0, self.box.width):
                self.addObstacle(i, j)

    def __init__(self, number_of_cols, number_of_lines):
        self.entry_point = random_entry_point(number_of_cols, number_of_lines)
        self.text_areas = dict()
        self.obstacles_label = dict()
        self.box = generate_random_box(number_of_cols, number_of_lines)
        QWidget.__init__(self)
        self.grid = QGridLayout()
        self.displayObstacles()
        self.addInterrogationPoints(self.box.height, self.box.width)
        self.addButtons(self.box.height, self.box.width)
        self.solutions = self.box.find_exits(self.entry_point)

    def display(self):
        self.setLayout(self.grid)
        self.setWindowTitle("LaserBeam")
        self.show()

    def clear(self):
        for key, label in self.obstacles_label.items():
                label.setPixmap(QPixmap(os.getcwd() + "/gui/images/aether.png"))
        for key, textarea in self.text_areas.items():
            textarea.setText(' ')
        direction, letter = self.entry_point
        x = letter_to_int[letter]+3
        y = x
        if direction == '>':
            y = 0
        elif direction == '<':
            y = self.box.width+4
        elif direction == 'v':
            x = 0
        elif direction == '^':
            x = self.box.height+4
        else:
            raise ValueError("incorrect direction")
        self.text_areas[x, y].setText(direction)