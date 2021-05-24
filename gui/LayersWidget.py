from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QApplication, QStyleFactory, QVBoxLayout, QLabel, \
    QPushButton

from gui.OtsuWidget import OtsuWidget


class LayerWidget(QWidget):
    def __init__(self, parent, index, title, layer):
        super(LayerWidget, self).__init__(parent)
        self.thresh = None
        self.index = index
        self.parent = parent
        self.layer = layer
        # w, h = self.layer.dimensions()
        # print(w)
        # print(h)
        layout = QHBoxLayout(self)
        self.setGeometry(280, 30, 0, 0)
        self.setLayout(layout)
        self.setStyleSheet("background:rgba(255,255,255,0.2)")
        self.title = QLabel(title)
        layout.addWidget(self.title)
        self.title.setStyleSheet("color:#e4e4e4; font-size:15px; text-transform:uppercase;"
                                 "letter-spacing:1px; width:290px; text-align:center;")
        self.title.setGeometry(150, 30, 0, 0)
        self.apply = QPushButton("T")
        self.apply.clicked.connect(self.apply_tresholding)
        self.apply.setGeometry(10, 0, 50, 50)
        self.apply.setStyleSheet("background-color:#2c2c2c; "
                                 "color:#e4e4e4;")
        layout.addWidget(self.apply)

    def apply_tresholding(self):
        self.thresh = OtsuWidget(self, self.layer)
        self.thresh.show()

    def apply_update(self):
        print("LayerWidget")
        self.parent.apply_update()


class LayersWidget(QWidget):
    def __init__(self, parent, layers):
        super(LayersWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.setGeometry(300, 400, 0, 0)
        self.setLayout(self.layout)
        # self.setStyleSheet("border: 1px solid white")
        self.parent = parent
        self.layers = layers
        self.layout_widgets = []

    def add_layer_widget(self, index, layer):
        print("Add")
        title = "Layer " + str(index)
        widget = LayerWidget(self, index, title, layer)
        print("ADDed")
        self.layout_widgets.append(widget)
        print("something 1")
        self.layout.addWidget(widget)
        print("something 2")

    def apply_update(self):
        print("LayersWidget")
        self.parent.apply_update()
