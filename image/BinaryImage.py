from PIL import Image, ImageFilter
import numpy as np
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap, QImage

from image.Layer import Layers


class BinaryImage:
    def __init__(self):
        self.original_image = Image
        self.image = self.original_image
        self.image_array = []
        self.array = []
        self.width = 0
        self.height = 0
        self.layers_array = []
        self.layers = None

    def set_image(self, image_path):
        self.original_image = Image.open(image_path).convert('LA')
        self.width, self.height = self.original_image.size
        self.original_image.show()
        self.image = self.original_image
        self.image_array = np.asarray(self.image)
        self.array = np.array(self.image)
        self.layers = Layers(self)

    def array_to_image(self, image_path="tempImage.png"):
        self.image.show()
        img = Image.fromarray(self.image_array, 'LA')  # rgb?
        img.show()
        # img = Image.fromarray(np.uint8(self.image_array)).convert('RGB')
        img.save(image_path)

    def get_image(self):
        return self.image

    def pil2pixmap(self, img):
        im = img
        if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = img.convert("RGBA")
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
        pixmap = QPixmap.fromImage(qim)
        return pixmap

    def get_pixmap(self):
        return self.pil2pixmap(self.image)

    def blur(self):
        self.image = self.image.filter(ImageFilter.GaussianBlur)
        self.image_array = np.asarray(self.image)
        self.array = np.array(self.image)

    def show_image(self):
        self.image.show()

    def get_image_width(self):
        return self.width

    def get_image_height(self):
        return self.height

    def count_brightness(self, x, y, brightness):
        max_value = brightness[1]
        min_value = brightness[0]
        if(self.array[y, x, 0] >= min_value and self.array[y, x, 0] <= max_value):
            return True
        else:
            return False

    def add_layer(self, layer_array):
        max_value = 0
        min_value = 255
        for i in range(len(layer_array)):
            x = layer_array[i][0]
            y = layer_array[i][1]
            if(self.array[y, x, 0] >= max_value):
                max_value = self.array[y, x, 0]
            if(self.array[y, x, 0] <= min_value):
                min_value = self.array[y, x, 0]
        print(min_value)
        print(max_value)
        brightness = [min_value, max_value]
        n = self.layers.add(brightness)
        return n


