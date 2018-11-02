from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import pyqtSlot, Qt

class Cell(QLabel):
    def __init__(self, x, y, win):
        QLabel.__init__(self, win)
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

class ForwardSlashMirrorCell(Cell):
    def __init__(self, x, y, win):
        Cell.__init__(self, x, y, win)
        self.setPixmap(QPixmap(os.getcwd() + "/images/forward_slash_mirror.png"))

class BackSlashMirrorCell(Cell):
    def __init__(self, x, y, win):
        Cell.__init__(self, x, y, win)
        self.setPixmap(QPixmap(os.getcwd() + "/images/back_slash_mirror.png"))

class VerticalMirrorCell(Cell):
    def __init__(self, x, y, win):
        Cell.__init__(self, x, y, win)
        self.setPixmap(QPixmap(os.getcwd() + "/images/vertical_mirror.png"))

class HorizontalMirrorCell(Cell):
    def __init__(self, x, y, win):
        Cell.__init__(self, x, y, win)
        self.setPixmap(QPixmap(os.getcwd() + "/images/horizontal_mirror.png"))

class VerticalMirrorCell(Cell):
    def __init__(self, x, y, win):
        Cell.__init__(self, x, y, win)
        self.setPixmap(QPixmap(os.getcwd() + "/images/vertical_mirror.png"))

class SquareMirrorCell(Cell):
    def __init__(self, x, y, win):
        Cell.__init__(self, x, y, win)
        self.setPixmap(QPixmap(os.getcwd() + "/images/square_mirror.png"))

class AetherCell(Cell):
    def __init__(self, x, y, win):
        Cell.__init__(self, x, y, win)
        self.setPixmap(QPixmap(os.getcwd() + "/images/aether_mirror.png"))
