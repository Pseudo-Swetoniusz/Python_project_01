from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, \
    QFileDialog, QLineEdit, QSlider, QGridLayout, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QEvent

from gui import MainWindow
from gui.ImageWidget import ImageWidget


class MainFrame(QFrame):
    def __init__(self, parent: MainWindow):
        super(MainFrame, self).__init__(parent)

        # self.setFrameShape(QFrame.StyledPanel)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.window = parent
        self.image = ImageWidget(self)
        print(self.width())
        print(self.height())

    def set_image(self, image):
        self.image.set_image(image)

    def resizeEvent(self, e):
        self.image.update_margin()

    def enable_brush(self):
        self.image.enable_brush()

    def enable_rubber(self):
        self.image.enable_rubber()