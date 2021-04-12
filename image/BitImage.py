from PIL import Image
import numpy as np
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap, QImage


class BitImage:
    def __init__(self):
        self.original_image = Image
        self.image = self.original_image
        self.image_array = []

    def set_image(self, image_path):
        self.original_image = Image.open(image_path)
        self.original_image.show()
        self.image = self.original_image
        image_sequence = self.original_image.getdata()
        array = list(image_sequence)
        self.image_array = np.array(array)

    def array_to_image(self, image_path="tempImage.png"):
        img = Image.fromarray(self.image_array)  # rgb?
        # img = Image.fromarray(np.uint8(self.image_array)).convert('RGB')
        img.save(image_path)
        img.show()

    def get_image(self):
        return self.image

    def pil2pixmap(self, im):
        if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = im.convert("RGBA")
        # Bild in RGBA konvertieren, falls nicht bereits passiert
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
        pixmap = QPixmap.fromImage(qim)
        return pixmap

    def get_pixmap(self):
        return self.pil2pixmap(self.image)
