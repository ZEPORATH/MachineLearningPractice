import numpy as np
import matplotlib.pyplot as plt
import cv2

#import the necessaary packages
class RGBHistogram:
    def __init__(self, bins):
        #store the numbers of bins the histogram will use
        self.bins = bins

    def describe(self, image):
        #compute  a 3D Histogram in RGB colorspace
        #then normalize the hsitogram so that images
        #with the same content, but either scaled larger
        #or smaller will have (roughly) the same histogram
        hist = cv2.calcHist([image],[0,1,2],
                            None, self.bins,[0,256,0,256,0,256])
        hist = cv2.normalize(hist)

        #return out 3D histogram as a flattened array
        return hist.flatten()
    
