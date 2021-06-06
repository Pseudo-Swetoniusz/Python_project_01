
import numpy as np
from matplotlib import pyplot as plt

MAX_PIX = 256


def generateHist(layer): #generating histogram for defining automatic threshold
    x = np.arange(0, MAX_PIX)
    histogram = np.zeros(256)
    width, height = layer.dimensions()
    for i in range(height):
        for j in range(width):
            if layer.pixelInMask(i, j):
                histogram[layer.pixels[i][j][0]] += 1
    # plt.bar(x, histogram, color='b') #, width=5, align='center', alpha=0.25
    # plt.show()
    layer.histogram = histogram
    return histogram


def thresholdImage(layer, threshold): # returns an image with the thresholded layer
    # print("thresholdImage")
    width, height = layer.dimensions()
    result = np.zeros((height, width))
    for i in range(0, height):
        for j in range(0, width):
            if layer.pixelInMask(i, j):
                if layer.pixels[i][j][0] < threshold:
                    result[i][j] = 0
                else:
                    result[i][j] = MAX_PIX - 1
    return result


def weight(x, y, histogram, num): #histogram analysis for otsu - supporting function
    sum = 0
    for i in range(x, y):
        sum += histogram[i]
    sum = sum / num
    return sum


def mean(x, y, histogram):#histogram analysis for otsu - supporting function
    numerator = 0
    denominator = 0
    for i in range(x, y):
        numerator += (histogram[i] * i)
        denominator += histogram[i]
    if denominator == 0:
        return 0  # 0 case
    return numerator / denominator


def variance(x, y, histogram, mean):#histogram analysis for otsu - supporting function
    numerator = 0
    denominator = 0
    for i in range(x, y):
        denominator += histogram[i]
        diff = i - mean
        numerator += (diff * diff * histogram[i])
    if denominator == 0:
        return 0  # 0 case
    return numerator / denominator


def withinClassVariance(x, y, histogram, num): #histogram analysis for otsu
    background = (weight(x, y, histogram, num), variance(x, y, histogram, mean(x, y, histogram)))
    foreground = (weight(y, MAX_PIX, histogram, num), variance(y, MAX_PIX, histogram, mean(y, MAX_PIX, histogram)))
    var = background[0] * background[1] + foreground[0] * foreground[1]
    return var


def calculateThreshold(histogram, num): #calculate threshold value based on histogram
    minWCV = withinClassVariance(0, 1, histogram, num)
    threshold = 1
    for i in range(2, MAX_PIX):
        wcv = withinClassVariance(0, i, histogram, num)
        if wcv < minWCV:
            minWCV = wcv
            threshold = i
    return threshold


def automaticThreshold(layer): #find automatic threshold value (using otsu)
    histogram = generateHist(layer)
    width, height = layer.dimensions()
    threshold = calculateThreshold(histogram, width * height)
    return threshold


def automaticThreshold_for_gui(layer, hist):
    width, height = layer.dimensions()
    threshold = calculateThreshold(hist, width * height)
    return threshold


def otsu(layer, threshold=None): # main function, returns image with a thresholded layer
    print("otsu - in otsu")
    if threshold == None:
        threshold = automaticThreshold(layer)
    layer.threshold = threshold
    print(threshold)
    resultImage = thresholdImage(layer, threshold)
    return resultImage
