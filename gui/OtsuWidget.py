from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, \
    QFileDialog, QLineEdit, QSlider, QGridLayout, QDockWidget, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from thresholding.otsu import generateHist


class OtsuWidget(QWidget):
    def __init__(self, layer):
        super(OtsuWidget, self).__init__()
        self.setGeometry(500, 300, 0, 0)
        self.setStyleSheet("background:#3a3a3a; border: 2px solid #323232;")
        self.layer = layer
        # self.hist = generateHist(self.layer)
