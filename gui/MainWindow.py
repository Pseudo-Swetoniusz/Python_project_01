from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QApplication, QStyleFactory

from gui.LayersFrame import LayersFrame
from gui.MainFrame import MainFrame
from gui.ToolsFrame import ToolsFrame
from image.BinaryImage import BinaryImage
from PIL import Image


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.left = ToolsFrame(self)
        self.center = MainFrame(self)
        self.right = LayersFrame(self)
        self.image = BinaryImage()
        self.initUI()
        self.showMaximized()
        self.show()

    def initUI(self):
        widget = QWidget(self)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)
        layout.addWidget(self.left)
        layout.addWidget(self.center)
        layout.addWidget(self.right)
        self.setCentralWidget(widget)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.setGeometry(60, 0, 400, 400)
        self.setWindowTitle('Python_project_01')
        self.setStyleSheet("background:#4f4f4f;")


    def choose_image(self, scr):
        self.image.set_image(scr)
        self.center.set_image(self.image)
        layer_0 = self.image.get_layer(0)
        self.right.add_layer_widget(0, layer_0)

    def save_image(self):
        self.image.array_to_image()

    def enable_brush(self):
        self.center.enable_brush()

    def enable_rubber(self):
        self.center.enable_rubber()

    def apply_blur(self):
        self.image.blur()
        self.image.show_image()
        self.center.update_image()

    def add_layer(self):
        index, layer = self.center.add_layer()
        self.right.add_layer_widget(index, layer)

    def apply_update(self):
        self.center.update_image()
