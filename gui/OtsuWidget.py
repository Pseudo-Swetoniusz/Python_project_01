import numpy as np
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, \
    QFileDialog, QLineEdit, QSlider, QGridLayout, QDockWidget, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure

from thresholding.otsu import generateHist, automaticThreshold_for_gui


class OtsuWidget(QWidget):
    def __init__(self, parent, layer):
        super(OtsuWidget, self).__init__()
        self.parent = parent
        layout = QVBoxLayout()
        self.setGeometry(500, 300, 0, 0)
        self.setStyleSheet("background:#3a3a3a; border: 2px solid #323232;")
        self.layer = layer
        self.hist = generateHist(self.layer)
        x = np.arange(0, 256)
        self.figure = plt.figure()
        self.plt = self.figure.add_subplot(111)
        self.plt.bar(x, self.hist, color='b')
        self.n = automaticThreshold_for_gui(self.layer, self.hist)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setGeometry(0, 0, 375, 30)
        self.slider.valueChanged[int].connect(self.slider_changed_value)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.label_button_widget = QWidget()
        layout2 = QHBoxLayout()
        self.label1 = QLabel("Threshold value:")
        self.label1.setStyleSheet("color:#e4e4e4;")
        self.label2 = QLabel(str(self.n))
        self.label2.setStyleSheet("color:#e4e4e4;")
        self.button = QPushButton("Apply thresholding")
        self.button.clicked.connect(self.apply_tresholding)
        self.button.setStyleSheet("background-color:#2c2c2c; "
                                  "color:#e4e4e4;")
        layout2.addWidget(self.label1)
        layout2.addWidget(self.label2)
        layout2.addWidget(self.button)
        self.label_button_widget.setLayout(layout2)
        layout.addWidget(self.canvas)
        layout.addWidget(self.slider)
        layout.addWidget(self.label_button_widget)
        self.setLayout(layout)
        self.slider.setValue(self.n)
        self.resize(500, 300)
        self.show()

    def slider_changed_value(self, value):
        self.label2.setText(str(value))
        self.n = value

    def apply_tresholding(self):
        self.layer.otsu(self.n)
        self.parent.apply_update()
