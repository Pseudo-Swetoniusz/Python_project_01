import numpy as np
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, \
    QFileDialog, QLineEdit, QSlider, QGridLayout, QDockWidget, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure

from thresholding.otsu import generateHist


class OtsuWidget(QWidget):
    def __init__(self, layer):
        super(OtsuWidget, self).__init__()
        layout = QVBoxLayout()
        self.setGeometry(500, 300, 0, 0)
        self.setStyleSheet("background:#3a3a3a; border: 2px solid #323232;")
        self.layer = layer
        self.hist = generateHist(self.layer)
        x = np.arange(0, 256)
        self.figure = plt.figure()
        self.plt = self.figure.add_subplot(111)
        self.plt.bar(x, self.hist, color='b')
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setGeometry(0, 0, 375, 30)
        self.slider.valueChanged[int].connect(self.slider_changed_value)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        layout.addWidget(self.canvas)
        layout.addWidget(self.slider)
        self.setLayout(layout)
        self.resize(500,300)
        self.show()

    def slider_changed_value(self):
        print("change")