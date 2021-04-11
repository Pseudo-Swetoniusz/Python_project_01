from PIL import Image
import numpy as np


def imageToArray(imagePath):
    image = Image.open(imagePath)
    imageSequence = image.getdata()
    imageArray = np.array(imageSequence)
    return imageArray

def arrayToImage(imageArray,imagePath="tempImage.png"):
    img = Image.fromarray(imageArray, 'RGB') #rgb?
    img.save(imagePath)
    img.show()

