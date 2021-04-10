import numpy as np
from PIL import Image



def imageToArray(imagePath):
    image = Image.open(imagePath) # PIL.Image
    imageSequence = image.getdata()
    imageArray = np.array(imageSequence)
#     print("IMAGE ARRAY: \n",imageArray)
    return imageArray

def arrayToImage(imageArray,imagePath="tempImage.png"):
    img = Image.fromarray(imageArray, 'RGB') #rgb?
    img.save(imagePath)
    img.show()




# tested with the following:
# w, h = 512, 512
# data = np.zeros((h, w, 3), dtype=np.uint8)
# data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
# arrayToImage(data)

# imgArray = imageToArray("tempImage.png")
# print(imgArray)

#seems to work
