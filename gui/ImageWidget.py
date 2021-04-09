from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, \
    QFileDialog, QLineEdit, QSlider, QGridLayout, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class ImageWidget(QWidget):
    def __init__(self, parent):
        super(ImageWidget, self).__init__(parent)

        self.main = parent
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.image = QGraphicsScene()
        self.view = QGraphicsView(self.image)
        self.layout.addWidget(self.view)
        self.layout.setSpacing(0)

    def set_image(self, adress):
        pixmap = QPixmap(adress)
        w = pixmap.width()
        h = pixmap.height()
        print(w, h)
        print(self.main.width(), self.main.height())
        if w > self.main.width() and h > self.main.height():
            percent = 1.0
            while w > self.main.width() or h > self.main.height():
                w = percent * w
                h = percent * h
                percent = percent - 0.01
            print(w, h)
        pixmap_new = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        self.image.addPixmap(pixmap_new)
        self.image.update()
        print(self.image.width(), self.image.height())
        self.resize(self.image.width() + 50, self.image.height() + 50)
        m1 = (self.main.width() - self.image.width() - 50)/2
        m2 = (self.main.height() - self.image.height() - 50)/2
        self.move(m1, m2)
