from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, \
    QFileDialog, QLineEdit, QSlider, QGridLayout, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from gui import MainWindow


class ToolsFrame(QFrame):
    def __init__(self, parent: MainWindow):
        super(ToolsFrame, self).__init__(parent)

        # self.setFrameShape(QFrame.StyledPanel)
        self.window = parent
        self.setStyleSheet("background:#3a3a3a; border-right: 2px solid #323232;")
        self.setFixedWidth(60)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        layout.setAlignment(Qt.AlignTop)
        self.open_file = QPushButton()
        self.open_file.clicked.connect(self.open_file_name_dialog)
        self.open_file.setGeometry(10, 0, 50, 50)
        self.open_file.setStyleSheet("background-image: url(icons/icon1.png); background-color:#2c2c2c; "
                                     "background-size: cover; background-repeat: no-repeat; background-position: "
                                     "center;")
        layout.addWidget(self.open_file)

    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '/', "Image Files (*.png *.jpg *.jpeg *.bmp * "
                                                                            ".tif)")
        if file_name:
            print("ToolsFrame")
            self.window.choose_image(file_name[0])
