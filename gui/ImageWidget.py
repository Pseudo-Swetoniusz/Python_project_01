from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import Qt


class View(QGraphicsView):
    def __init__(self, img):
        super(View, self).__init__(img)
        self.brush = False
        self.rubber = False

    def enable_brush(self):
        if not self.brush:
            self.brush = True
            self.rubber = False
        else:
            self.brush = False

    def enable_rubber(self):
        if not self.rubber:
            self.rubber = True
            self.brush = False
        else:
            self.rubber = False

    def mouseMoveEvent(self, e):
        if self.brush:
            print("move brush")
            print(e.x(), e.y())
        elif self.rubber:
            print("move rubber")
            print(e.x(), e.y())
        else:
            print("move")
            print(e.x(), e.y())


class ImageWidget(QWidget):
    def __init__(self, parent):
        super(ImageWidget, self).__init__(parent)

        self.original_pixmap = QPixmap()
        self.current_pixmap = QPixmap()
        self.main = parent
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.image = QGraphicsScene()
        self.view = View(self.image)
        self.layout.addWidget(self.view)
        self.layout.setSpacing(0)
        self.setMouseTracking(True)

    def set_image(self, image):
        img = ImageQt(image)
        pixmap = QPixmap.fromImage(img)
        self.original_pixmap = pixmap
        w = pixmap.width()
        h = pixmap.height()
        if w > self.main.width() - 50 or h > self.main.height() - 50:
            percent = 0.99
            while w > self.main.width() - 50 or h > self.main.height() - 50:
                w = percent * w
                h = percent * h
                percent = percent - 0.01
        pixmap_new = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        self.current_pixmap = pixmap_new
        self.image.addPixmap(self.current_pixmap)
        self.image.update()
        self.resize(self.image.width() + 50, self.image.height() + 50)
        m1 = (self.main.width() - self.image.width() - 50) / 2
        m2 = (self.main.height() - self.image.height() - 50) / 2
        self.move(m1, m2)
        self.setGeometry(m1, m2, self.image.width() + 50, self.image.height() + 50)

    def update_margin(self):
        m1 = (self.main.width() - self.image.width() - 50) / 2
        m2 = (self.main.height() - self.image.height() - 50) / 2
        self.move(m1, m2)

    # def resize_pixmap(self, percent):
    #    w = percent * self.original_pixmap.width()
    #    h = percent * self.original_pixmap.height()
    #    pixmap_new = self.original_pixmap.scaled(w, h, Qt.KeepAspectRatio)
    #    self.current_pixmap = pixmap_new
    #    self.image.update()
    #    self.resize(self.image.width() + 50, self.image.height() + 50)
    #    m1 = (self.main.width() - self.image.width() - 50) / 2
    #    m2 = (self.main.height() - self.image.height() - 50) / 2
    #    self.move(m1, m2)

    def mouseMoveEvent(self, e):
        print("move")
        print(e.x(), e.y())

    def enable_brush(self):
        self.view.enable_brush()

    def enable_rubber(self):
        self.view.enable_rubber()
