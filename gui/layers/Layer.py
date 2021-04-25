import numpy as np
from otsu import otsu

class Layer:
    def __init__(self, brightness, number, layerAssigned, width, height):
        self.number = number
        self.pixels = layerAssigned
        self.brightness = brightness
        self.width = width
        self.height = height
        self.result = np.zeros((width,height))

    def pixelInMask(self,i,j):
        return (self.pixels[i][j]==self.number)

    def dimensions(self):
        return width,height

    def otsu(self,threshold=None):
        self.result=otsu(self,threshold)


class Layers:
    def __init__(self, image, layers = []):
        self.layer = layers
        if(self.layer==[]):
            self.layer.append(0)
        self.image = image
        self.width, self.height = image.shape
        self.layerAssigned = zeros((width,height))

    def add(self,newLayer):
        self.layer.append(newLayer)

    def remove(self,layer):
        self.layer.remove(layer)

    def size(self):
        return len(self.layer)

