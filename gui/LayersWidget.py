from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QApplication, QStyleFactory, QVBoxLayout

from gui.LayersFrame import LayersFrame
from gui.MainFrame import MainFrame
from gui.ToolsFrame import ToolsFrame
from image.BitImage import BitImage
from PIL import Image


class LayerWidget(QWidget):
    def __init__(self, parent, index):
        super(LayerWidget, self).__init__(parent)
        self.index = index
        self.parent = parent


class LayersWidget(QWidget):
    def __init__(self, parent, layers):
        super(LayersWidget, self).__init__(parent)

        layout = QVBoxLayout(self)
        self.setGeometry(290, 400, 0, 0)
        self.setLayout(layout)
        self.setStyleSheet("border: 1px solid white")
        self.parent = parent
        self.layers = layers
