from PIL import Image
import numpy as np


class BitImage:
    def __init__(self):
        self.original_image = Image
        self.image = self.original_image
        self.image_array = []

    def set_image(self, image_path):
        self.original_image = Image.open(image_path)
        #self.original_image.show()
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
