from PyQt5.QtWidgets import QFrame, QSizePolicy

from gui import MainWindow
from gui.ImageWidget import ImageWidget


class MainFrame(QFrame):
    def __init__(self, parent: MainWindow):
        super(MainFrame, self).__init__(parent)

        # self.setFrameShape(QFrame.StyledPanel)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.window = parent
        self.image = ImageWidget(self)

    def set_image(self, image):
        self.image.set_image(image)

    def resizeEvent(self, e):
        self.image.update_margin()

    def enable_brush(self):
        self.image.enable_brush()

    def enable_rubber(self):
        self.image.enable_rubber()

    def update_image(self):
        self.image.update_image()

    def add_layer(self):
        self.image.add_layer()