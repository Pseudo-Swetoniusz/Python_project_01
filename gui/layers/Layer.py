import numpy as np
from otsu import otsu

class Layer:
    def __init__(self, brightness, number=-1, layerAssigned=[], width=0, height=0, removed=False):
        self.number = number
        self.pixels = layerAssigned
        self.brightness = brightness
        self.width = width
        self.height = height
        self.result = np.zeros((width,height))
        self.removed=removed

    def pixelInMask(self,i,j):
        return (self.pixels[i][j]==self.number)

    def dimensions(self):
        return self.width, self.height

    def otsu(self,threshold=None):
        self.result=otsu(self,threshold)


class Layers:
    def __init__(self, image, layers = []):
        self.layer = layers
        if(self.layer==[]):
            self.layer.append(0)
        self.image = image
        self.width, self.height = image.shape
        self.layerAssigned = np.zeros((self.width, self.height))

    def add(self, brightness):
        newNumber=len(self.layers)
        newLayer=Layer(brightness, newNumber, self.layerAssigned, self.width, self.height)
        self.layers.append(newLayer)
        for i in range(self.width):
            for j in range(self.height):
                pixel=self.image[i][j]
                pixLayer=self.layerAssigned[i][j]
                if(pixel>=brightness[0] and pixel<=brightness[1] and (pixLayer==0 or pixLayer.removed==True)):
                    self.layerAssigned[i][j]=newNumber

    def remove(self,layer):
        for i in range(self.width):
            for j in range(self.height):
                if (self.layerAssigned[i][j] == layer.number):
                    self.layerAssigned[i][j] = 0
        layer.removed=True

    def toArray(self):
        array=np.zeros((self.width,self.height))
        for i in range(self.width):
            for j in range(self.height):
                layer=self.layerAssigned[i][j]
                pixel=layer.result[i][j]
                array[i][j]=pixel
        return array
        
    def size(self):
        return len(self.layer)

