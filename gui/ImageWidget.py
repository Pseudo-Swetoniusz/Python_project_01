from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt


class View(QGraphicsView):
    def __init__(self, parent, img):
        super(View, self).__init__(img)
        self.brush = False
        self.rubber = False
        self.parent = parent
        self.canvas1 = QPixmap(self.parent.image_width, self.parent.image_height)

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
            # print("move brush")
            # print(e.x(), e.y())
            pixmap = self.parent.canvas.pixmap()
            painter = QPainter(pixmap)
            painter.drawPoint(e.x(), e.y())
            painter.end()
            self.parent.canvas.setPixmap(pixmap)
            # self.parent.image.addPixmap(self.parent.canvas)
            el = [e.x(), e.y()]
            self.parent.append_to_layer(el)


class ImageWidget(QWidget):
    def __init__(self, parent):
        super(ImageWidget, self).__init__(parent)

        self.img = None
        self.image_width = None
        self.image_height = None
        self.layer_array = []
        self.original_pixmap = QPixmap()
        self.current_pixmap = QPixmap()
        self.pixmap = QGraphicsPixmapItem()
        self.canvas = QGraphicsPixmapItem()
        # self.label = QLabel()
        # self.label.setPixmap(self.canvas)
        self.main = parent
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.image = QGraphicsScene()
        self.image.addItem(self.pixmap)
        self.image.addItem(self.canvas)
        self.view = View(self, self.image)
        self.view.setScene(self.image)
        self.layout.addWidget(self.view)
        self.layout.setSpacing(0)
        self.setMouseTracking(True)
        # self.view.setMouseTracking(True)

    def set_image(self, image):
        self.img = image
        self.original_pixmap = image.get_pixmap()
        pix = self.original_pixmap
        w = pix.width()
        h = pix.height()
        if w > self.main.width() - 50 or h > self.main.height() - 50:
            percent = 0.99
            while w > self.main.width() - 50 or h > self.main.height() - 50:
                w = percent * w
                h = percent * h
                percent = percent - 0.01
        pixmap_new = pix.scaled(w, h, Qt.KeepAspectRatio)
        self.image_width = w
        self.image_height = h
        self.current_pixmap = pixmap_new
        self.pixmap.setPixmap(self.current_pixmap)
        canvas_map = QPixmap(w, h)
        canvas_map.fill(QColor(0, 0, 0, 0))
        self.canvas.setPixmap(canvas_map)
        self.image.update()
        self.view.update()
        # self.image.update()
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

    def enable_brush(self):
        self.view.enable_brush()

    def enable_rubber(self):
        self.view.enable_rubber()

    def update_image(self):
        pix = self.img.get_pixmap()
        pix = pix.scaled(self.image_width, self.image_height, Qt.KeepAspectRatio)
        self.pixmap.setPixmap(pix)

    def append_to_layer(self, element):
        self.layer_array.append(element)

    def add_layer(self):
        print("image widget - add layer")
        layer_array_new = []
        scale = self.img.get_image_width() / self.image_width
        for i in range(len(self.layer_array)):
            x = self.layer_array[i][0] * scale
            y = self.layer_array[i][1] * scale
            el = [int(x), int(y)]
            layer_array_new.append(el)
        index, layer = self.img.add_layer(layer_array_new)
        self.layer_array = []
        canvas_map = QPixmap(self.image_width, self.image_height)
        canvas_map.fill(QColor(0, 0, 0, 0))
        self.canvas.setPixmap(canvas_map)
        return index, layer
