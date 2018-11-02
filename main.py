# /gui/main.py
import sys
from PyQt5.QtWidgets import QApplication
from gui.window import Window
from PyQt5.QtCore import QEventLoop, QTimer

number_of_lines = 7
number_of_cols = 8


app = QApplication(sys.argv)
win = Window(number_of_cols, number_of_lines)
win.display()
loop = QEventLoop()
QTimer.singleShot(5000, loop.quit)
loop.exec_()
win.clear()
win.display()
sys.exit(app.exec_())
