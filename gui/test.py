from PyQt5.QtWidgets import QDialog, QWidget
# class ImageGallery(QDialog):
#
#     def __init__(self, parent=None):
#         super(QDialog, self).__init__(parent)
#         self.setWindowTitle("Image Gallery")
#         self.setLayout(QGridLayout(self))
#
#     def populate(self, pics, size, imagesPerRow=4):
#         row = col = 0
#         for pic in pics:
#             label = ImageLabel("")
#             pixmap = QPixmap(pic)
#             pixmap = pixmap.scaled(size, flags)
#             label.setPixmap(pixmap)
#             self.layout().addWidget(label, row, col)
#             col +=1
#             if col % imagesPerRow == 0:
#                 row += 1
#                 col = 0
# import sys
# import os
#
# class InformationBox(QWidget):
#     def __init__(self):
#
#         self.setWindowTitle("LaserBeam")
#         self.title = QLabel("Browthon")
#         self.description = QLabel(self.main.versionAll + "\nCréé par PastaGames \nGithub : https://github.com/LavaPower/Browthon")
#         self.grid = QGridLayout()
#         self.grid.addWidget(self.title, 1, 1, 1, 2)
#         self.imageLabel = QLabel()
#         self.image = QPixmap("./images/aether.png")
#         self.imageLabel.setPixmap(self.image)
#         self.grid.addWidget(self.imageLabel, 2, 1, 1, 1)
#         self.grid.addWidget(self.description, 2, 2, 1, 1)
#         self.setLayout(self.grid)
#
#     def display(self):
#         app = QApplication(sys.argv)
#         self.show()
#         sys.exit(app.exec_())


# importations à faire pour la réalisation d'une interface graphique
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# # Première étape : création d'une application Qt avec QApplication
# #    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
# #    on vérifie s'il existe déjà une instance de QApplication
# app = QApplication.instance()
# if not app: # sinon on crée une instance de QApplication
#     app = QApplication(sys.argv)
#
# # création d'une fenêtre avec QWidget dont on place la référence dans fen
# fen = QWidget()
#
# # la fenêtre est rendue visible
# fen.show()
#
# # exécution de l'application, l'exécution permet de gérer les événements
# app.exec_()
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# app = QApplication.instance()
# if not app:
#     app = QApplication(sys.argv)
#
# fen = QWidget()
#
# # on donne un titre à la fenêtre
# fen.setWindowTitle("LaserBeam")
#
# # on fixe la taille de la fenêtre
# fen.resize(500,500)
#
# # on fixe la position de la fenêtre
# #fen.move(300,50)
#
# fen.show()
#
# app.exec_()
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# class Fenetre(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.setWindowTitle("Ma fenetre")
#
# app = QApplication.instance()
# if not app:
#     app = QApplication(sys.argv)
#
# fen = Fenetre()
# fen.show()
#
# app.exec_()

# import sys
# import time
#
# from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
#                           QThreadPool, pyqtSignal)
#
#
# # Subclassing QThread
# # http://qt-project.org/doc/latest/qthread.html
# class AThread(QThread):
#
#     def run(self):
#         count = 0
#         while count < 5:
#             time.sleep(1)
#             print("A Increasing")
#             count += 1
#
# # Subclassing QObject and using moveToThread
# # http://blog.qt.digia.com/blog/2007/07/05/qthreads-no-longer-abstract
# class SomeObject(QObject):
#
#     finished = pyqtSignal()
#
#     def long_running(self):
#         count = 0
#         while count < 5:
#             time.sleep(1)
#             print("B Increasing")
#             count += 1
#         self.finished.emit()
#
# # Using a QRunnable
# # http://qt-project.org/doc/latest/qthreadpool.html
# # Note that a QRunnable isn't a subclass of QObject and therefore does
# # not provide signals and slots.
# class Runnable(QRunnable):
#
#     def run(self):
#         count = 0
#         app = QCoreApplication.instance()
#         while count < 5:
#             print("C Increasing")
#             time.sleep(1)
#             count += 1
#         app.quit()
#
#
# def using_q_thread():
#     app = QCoreApplication([])
#     thread = AThread()
#     thread.finished.connect(app.exit)
#     thread.start()
#     sys.exit(app.exec_())
#
# def using_move_to_thread():
#     app = QCoreApplication([])
#     objThread = QThread()
#     obj = SomeObject()
#     obj.moveToThread(objThread)
#     obj.finished.connect(objThread.quit)
#     objThread.started.connect(obj.long_running)
#     objThread.finished.connect(app.exit)
#     objThread.start()
#     sys.exit(app.exec_())
#
# def using_q_runnable():
#     app = QCoreApplication([])
#     runnable = Runnable()
#     QThreadPool.globalInstance().start(runnable)
#     sys.exit(app.exec_())
#
# if __name__ == "__main__":
#     #using_q_thread()
#     #using_move_to_thread()
#     using_q_runnable()
#
# from PIL import Image, ImageDraw
#
# class Grid:
#
#     def __init__(self):
#         self.capture_image()
#
#     def capture_image(self):
#         screenshot = Image.open("screenshots/screen_staging.png")
#         columns = 60
#         rows = 80
#         screen_width, screen_height = screenshot.size
#
#         block_width = ((screen_width - 1) // columns) + 1 # this is just a division ceiling
#         block_height = ((screen_height - 1) // rows) + 1
#
#         for y in range(0, screen_height, block_height):
#             for x in range(0, screen_width, block_width):
#                 draw = ImageDraw.Draw(screenshot)
#                 draw.rectangle((x, y, x+block_width, y+block_height), outline = "red")
#
#         screenshot.save("grid.png")
#
#
# Grid()

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('./images/aether.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
