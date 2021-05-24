from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QFileDialog, QFrame, QSizePolicy
from PyQt5.QtCore import Qt

from gui import MainWindow


class ToolsFrame(QFrame):
    def __init__(self, parent: MainWindow):
        super(ToolsFrame, self).__init__(parent)

        # self.setFrameShape(QFrame.StyledPanel)
        self.window = parent
        self.setStyleSheet("background:#3a3a3a; border-right: 2px solid #323232;")
        self.setFixedWidth(160)
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
        self.blur = QPushButton("Gaussian Blur")
        self.blur.clicked.connect(self.apply_blur)
        self.blur.setGeometry(10, 0, 50, 50)
        self.blur.setStyleSheet("background-color:#2c2c2c; "
                                "background-size: cover; background-repeat: no-repeat; background-position: "
                                "center; color:#e4e4e4;")
        layout.addWidget(self.blur)
        self.brush = QPushButton("Brush")
        self.brush.clicked.connect(self.enable_brush)
        self.brush.setGeometry(10, 0, 50, 50)
        self.brush.setStyleSheet("background-color:#2c2c2c; "
                                 "background-size: cover; background-repeat: no-repeat; background-position: "
                                 "center; color:#e4e4e4;")
        layout.addWidget(self.brush)
        
        self.add = QPushButton("Add Layer")
        self.add.clicked.connect(self.add_layer)
        self.add.setGeometry(10, 0, 50, 50)
        self.add.setStyleSheet("background-color:#2c2c2c; "
                               "background-size: cover; background-repeat: no-repeat; background-position: "
                               "center; color:#e4e4e4;")
        layout.addWidget(self.add)
        self.save = QPushButton("Save File")
        self.save.clicked.connect(self.save_file)
        self.save.setGeometry(10, 0, 50, 50)
        self.save.setStyleSheet("background-color:#2c2c2c; "
                                "background-size: cover; background-repeat: no-repeat; background-position: "
                                "center; color:#e4e4e4;")
        layout.addWidget(self.save)

    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '/', "image Files (*.png *.jpg *.jpeg *.bmp * "
                                                                        ".tif)")
        if file_name[0] == '':
            print("No image")
        elif file_name:
            self.window.choose_image(file_name[0])
        else:
            print("No image")

    def enable_brush(self):
        self.window.enable_brush()

    def enable_rubber(self):
        self.window.enable_rubber()

    def add_layer(self):
        self.window.add_layer()

    def save_file(self):
        self.window.save_image()

    def apply_blur(self):
        self.window.apply_blur()
