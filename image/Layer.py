import numpy as np
from PIL import Image, ImageFilter
from thresholding import otsu

class Layer:
    def __init__(self, brightness, number=-1, layerAssigned=[], width=0, height=0, removed=False):
        self.number = number
        self.pixels = layerAssigned
        self.brightness = brightness
        self.width = width
        self.height = height
        self.result = np.zeros((self.width, self.height))
        self.removed = removed
        print("created layer")

    def pixelInMask(self,i,j):
        return (self.pixels[i][j]==self.number)

    def dimensions(self):
        return self.width, self.height

    def otsu(self,threshold=None):
        self.result=otsu(self,threshold)


class Layers:
    def __init__(self, image, layers = []):
        self.layers = layers
        if(self.layers==[]):
            self.layers.append(0)
        self.image = image
        self.width = self.image.get_image_width()
        self.height = self.image.get_image_height()
        self.layerAssigned = np.zeros((self.width, self.height))

    def add(self, brightness):
        print("adding layer")
        newNumber = len(self.layers)
        print(newNumber)
        newLayer = Layer(brightness, newNumber, self.layerAssigned, self.width, self.height)
        self.layers.append(newLayer)
        print("appended layer")
        for i in range(self.width):
            for j in range(self.height):
                # pixel=self.image[i][j]
                pixLayer=self.layerAssigned[i][j]
                # layer = self.layers.
                if(self.image.count_brightness(i, j, brightness) and pixLayer==0):
                    self.layerAssigned[i][j] = newNumber
        print("layer added")



    def remove(self,layer):
        for i in range(self.width):
            for j in range(self.height):
                if (self.layerAssigned[i][j] == layer.number):
                    self.layerAssigned[i][j] = 0
        layer.removed=True

    def size(self):
        return len(self.layer)
