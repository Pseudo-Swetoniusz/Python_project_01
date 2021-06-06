import numpy as np
from PIL import Image, ImageFilter
from thresholding import otsu


class Layer:
    def __init__(self, parent, brightness, number=-1, image=[], layerAssigned=[], width=0, height=0, removed=False):
        self.parent = parent
        self.number = number # unique number of this layer
        self.pixels = image
        self.pixels_org = image
        self.layerAssigned = layerAssigned
        self.brightness = brightness # layer includes pixels of defined brightness from brightness[0] to brightness[1]
        self.width = width
        self.height = height
        self.result = [[self.pixels[i][j][0] for j in range(width)] for i in range(height)] # result array (will be updated during thresholding through self.otsu())
        self.removed = removed
        self.histogram = [] # calculated histogram
        self.threshold = None # value of threshold

    def pixelInMask(self, i, j): # True - pixel belongs to this layer; False - it doesn't belong
        return self.layerAssigned[i][j] == self.number

    def dimensions(self):
        return self.width, self.height

    def otsu(self, threshold=None): # called when layer is to be thresholded
        self.result = otsu.otsu(self, threshold)
        self.pixels = self.pixels_org
        self.parent.update_image()

    def update_array(self, array):
        self.pixels = array
        self.pixels_org = array


class Layers: # a collection of layers in our application
    def __init__(self, image, image_array, layers=[]):
        self.image = image # image loaded
        self.image_array = image_array 
        self.layers = layers # array of existing layers
        self.width = self.image.get_image_width()
        self.height = self.image.get_image_height()
        self.layerAssigned = np.zeros((self.height, self.width)) # array denoting which pixel belongs to which array
        brightness0 = [0, 255]
        newLayer0 = Layer(self, brightness0, 0, self.image_array, self.layerAssigned, self.width, self.height)
        if self.layers == []:
            self.layers.append(newLayer0) # autimatically included at least one layer

    def add(self, brightness): # add layer
        newNumber = len(self.layers)
        newLayer = Layer(self, brightness, newNumber, self.image_array, self.layerAssigned, self.width, self.height)
        self.layers.append(newLayer)
        for i in range(self.height):
            for j in range(self.width):
                pixLayer = self.layerAssigned[i][j]
                if self.image.count_brightness(i, j, brightness) and pixLayer == 0:
                    self.layerAssigned[i][j] = newNumber
        return newNumber, newLayer

    def get_layer(self, index):
        layer = self.layers[index]
        return layer

    def remove(self, layer):
        for i in range(self.width):
            for j in range(self.height):
                if self.layerAssigned[i][j] == layer.number:
                    self.layerAssigned[i][j] = 0
        layer.removed = True

    def toArray(self): # converts all layers to one array 
        array = np.zeros((self.height, self.width))
        for i in range(self.height):
            for j in range(self.width):
                layer = self.layerAssigned[i][j]
                print(layer)
                layer1 = self.layers[int(layer)]
                pixel = layer1.result[i][j]
                print(pixel)
                array[i][j] = int(pixel)
        return array

    def size(self):
        return len(self.layer)

    def update_image(self):
        array = self.toArray()
        #self.image.count_brightness(1, 1, [0, 255])
        #self.image.p_s()
        self.image.update_self(array)

    def update_array(self, array):
        self.image_array = array
        for i in range(len(self.layers)):
            self.layers[i].update_array(array)
