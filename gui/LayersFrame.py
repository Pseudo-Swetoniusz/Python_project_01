from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, \
    QFileDialog, QLineEdit, QSlider, QGridLayout, QDockWidget, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from gui.LayersWidget import LayersWidget


class LayersFrame(QFrame):
    def __init__(self, parent):
        super(LayersFrame, self).__init__(parent)

        self.setStyleSheet("background:#3a3a3a; border-left: 2px solid #323232;")
        self.setFixedWidth(300)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)
        self.title = QLabel("Layers")
        self.title.setStyleSheet("color:#e4e4e4; font-size:20px; text-transform:uppercase;"
                                 "letter-spacing:1px;")
        layout.addWidget(self.title)
        self.layers_widget = LayersWidget(self, None)
        layout.addWidget(self.layers_widget)

    def add_layer_widget(self, index, layer):
        self.layers_widget.add_layer_widget(index, layer)

