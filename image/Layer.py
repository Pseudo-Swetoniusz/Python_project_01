import numpy as np
from PIL import Image, ImageFilter
from thresholding import otsu


class Layer:
    def __init__(self, brightness, number=-1, image=[], layerAssigned=[], width=0, height=0, removed=False):
        self.number = number
        self.pixels = image
        self.layerAssigned = layerAssigned
        self.brightness = brightness
        self.width = width
        self.height = height
        # self.result = np.zeros((self.width, self.height))
        self.result = np.zeros((self.height, self.width))
        self.removed = removed
        self.histogram = []
        self.threshold = None

    def pixelInMask(self, i, j):
        return self.layerAssigned[i][j] == self.number

    def dimensions(self):
        return self.width, self.height

    def otsu(self, threshold=None):
        print("otsu")
        self.result = otsu.otsu(self, threshold)
        print("otsu - end")


class Layers:
    def __init__(self, image, image_array, layers=[]):
        self.image = image
        self.image_array = image_array
        self.layers = layers
        self.width = self.image.get_image_width()
        self.height = self.image.get_image_height()
        #self.layerAssigned = np.zeros((self.width, self.height))
        self.layerAssigned = np.zeros((self.height, self.width))
        brightness0 = [0, 255]
        newLayer0 = Layer(brightness0, 0, self.image_array, self.layerAssigned, self.width, self.height)
        if self.layers == []:
            self.layers.append(newLayer0)

    def add(self, brightness):
        newNumber = len(self.layers)
        newLayer = Layer(brightness, newNumber, self.image_array, self.layerAssigned, self.width, self.height)
        self.layers.append(newLayer)
        #for i in range(self.width):
        #    for j in range(self.height):
        #        # pixel=self.image[i][j]
        #        pixLayer = self.layerAssigned[i][j]
        #        # layer = self.layers.
        #        if self.image.count_brightness(i, j, brightness) and pixLayer == 0:
        #            self.layerAssigned[i][j] = newNumber
        for i in range(self.height):
            for j in range(self.width):
                # pixel=self.image[i][j]
                pixLayer = self.layerAssigned[i][j]
                # layer = self.layers.
                if self.image.count_brightness(i, j, brightness) and pixLayer == 0:
                    self.layerAssigned[i][j] = newNumber
        return newNumber, newLayer

    def get_layer(self, index):
        layer = self.layers[index]
        return layer

    def remove(self, layer):
        for i in range(self.width):
            for j in range(self.height):
                if (self.layerAssigned[i][j] == layer.number):
                    self.layerAssigned[i][j] = 0
        layer.removed = True

    def size(self):
        return len(self.layer)
