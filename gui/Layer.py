import numpy as np

class Layer:
    def __init__(self, imageArray, activeArray):
        self.imageArray = imageArray
        self.activeArray = activeArray

    def pixelInMask(self,i,j):
        return self.activeArray[i][j]


class Layers:
    def __init__(self,layers = []):
        self.layer = layers

    def add(self,newLayer):
        self.layer.append(newLayer)

    def remove(self,layer):
        self.layer.remove(layer)
        
    def size(self):
        return len(self.layer)
