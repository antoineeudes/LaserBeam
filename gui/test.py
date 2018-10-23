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
import sys
import os

class InformationBox(QWidget):
    def __init__(self):

        self.setWindowTitle("LaserBeam")
        self.title = QLabel("Browthon")
        self.description = QLabel(self.main.versionAll + "\nCréé par PastaGames \nGithub : https://github.com/LavaPower/Browthon")
        self.grid = QGridLayout()
        self.grid.addWidget(self.title, 1, 1, 1, 2)
        self.imageLabel = QLabel()
        self.image = QPixmap("./images/aether.png")
        self.imageLabel.setPixmap(self.image)
        self.grid.addWidget(self.imageLabel, 2, 1, 1, 1)
        self.grid.addWidget(self.description, 2, 2, 1, 1)
        self.setLayout(self.grid)

    def display(self):
        app = QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())
