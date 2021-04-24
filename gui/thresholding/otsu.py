import numpy as np

MAX_PIX=256


def generateHist(image):
    x=np.arange(0,MAX_PIX)
    histogram=np.zeros(MAX_PIX)
    width,height=image.shape
    for i in range(width):
        for j in range(height):
            histogram[image[i][j]]+=1
    plt.bar(x, histogram, color='b', width=5, align='center', alpha=0.25)
    plt.show()
    return histogram

def thresholdImage(image,threshold):
    width, height = image.shape
    result=np.zeros((width,height))
    for i in range(0,width):
        for j in range(0,height):
            if (image[i][j]<threshold)
                result[i][j]=0
            else
                result[i][j]=MAX_PIX-1

    return result

def weight(x,y,histogram,num):
    sum=0
    for i in range(x,y):
        sum+=histogram[i]
    sum=sum/num
    return sum

def mean(x,y,histogram):
    numerator=0
    denominator=0
    for i in range(x, y):
        numerator+=(histogram[i]*i)
        denominator+=histogram[i]
    if(denominator==0):
        return 0            #0 case!!!
    return numerator/denomiator

def variance(x,y,histogram,mean):
    numerator = 0
    denominator = 0
    for i in range(x, y):
        denominator += histogram[i]
        diff=i-mean
        numerator+=(diff*diff*histogram[i])
    if (denominator == 0):
        return 0  # 0 case!!!!!!!!
    return numerator/denominator

def withinClassVariance(x,y,histogram,num):
    background=(weight(x,y,histogram,num),variance(x,y,histogram,mean(x,y,histogram)))
    foreground=(weight(y,MAX_PIX,histogram,num),variance(y,MAX_PIX,histogram,mean(y,MAX_PIX,histogram)))
    var=background[0]*background[1]+foreground[0]*foreground[1]
    return var

def calculateThreshold(histogram,num):
    minWCV=withinClassVariance(0,1,histogram,num)
    threshold=1
    for i in range(2,MAX_PIX):
        wcv=withinClassVariance(0,i,histogram,num)
        if(wcv<minWCV):
            minWCV=wcv
            threshold=i
    return threshold


def automaticThreshold(image):
    histogram=generateHist(image)
    width, height = image.shape
    threshold=calculateThreshold(histogram,width*height)

def otsu(image,threshold=None):
    if(threshold==None):
        threshold=automaticThreshold(image)
    resultImage=thresholdImage(image,threshold)
    return resultImage
