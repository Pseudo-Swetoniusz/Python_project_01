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
        self.center.add_layer()
