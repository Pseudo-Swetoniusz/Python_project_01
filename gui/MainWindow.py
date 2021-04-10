from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QHBoxLayout, QVBoxLayout, QSplitter, QApplication, \
    QStyleFactory, QFrame

from gui.LayersFrame import LayersFrame
from gui.MainFrame import MainFrame
from gui.ToolsFrame import ToolsFrame


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.left = ToolsFrame(self)
        self.center = MainFrame(self)
        self.right = LayersFrame(self)
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
        print("Main Window")
        self.center.set_image(scr)
