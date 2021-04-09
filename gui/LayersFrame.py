from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, \
    QFileDialog, QLineEdit, QSlider, QGridLayout, QDockWidget, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class LayersFrame(QFrame):
    def __init__(self, parent):
        super(LayersFrame, self).__init__(parent)

        self.setStyleSheet("background:#3a3a3a; border-left: 2px solid #323232;")
        self.setFixedWidth(300)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

