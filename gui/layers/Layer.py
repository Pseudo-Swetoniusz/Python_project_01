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



w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:256, 0:256] = [255, 0, 0]
active = [[False for i in range(w)] for i in range(h)]
for i in range(w):
    for j in range(h):
        if(j<400 and j>100 and i>50 and i<450):
            active[i][j]=True