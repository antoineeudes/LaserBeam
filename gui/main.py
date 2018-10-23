import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()
    pic = QLabel(win)

    #use full ABSOLUTE path to the image, not relative
    pic.setPixmap(QPixmap(os.getcwd() + "/images/aether.png"))

    for i in range(1,5):
      for j in range(1,5):
         grid.addWidget(pic,i,j)

    win.setLayout(grid)
    win.setGeometry(100,100,200,100)
    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
