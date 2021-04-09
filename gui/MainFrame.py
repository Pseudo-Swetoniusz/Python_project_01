from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, \
    QFileDialog, QLineEdit, QSlider, QGridLayout, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from gui import MainWindow
from gui.ImageWidget import ImageWidget


class MainFrame(QFrame):
    def __init__(self, parent: MainWindow):
        super(MainFrame, self).__init__(parent)

        # self.setFrameShape(QFrame.StyledPanel)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.window = parent
        self.image = ImageWidget(self)

    def set_image(self, scr):
        self.image.set_image(scr)
