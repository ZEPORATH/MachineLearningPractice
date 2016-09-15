import cv2 as cv2
import os
from matplotlib import pyplot as plt
import numpy as np

#assign a path to image
path = 'C:/Users/Shahsank.Shekhar/Downloads/flipkart.jpg'
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

#check if the image is read or not
while not os.path.isfile(path):
    pass
img = cv2.imread(path,-1)
cv2.imshow('image',img)

#convert the image to grayscale and reepresent an histogram
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

hist = cv2.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0,256])

#computing a flattened Color Histogram
#grab the image channels , initalize the tuple of colors,
#the figure and aflattened feature vector

chans = cv2.split(img)
colors = ('b','g','r')
plt.figure()
plt.title("'Flattened' color histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
features = []
#loop over the image channels

for (chan,color) in zip(chans,colors):
    #create a histogram for the current channel and
    #concatenate the resulting histogram for each
    #channel
    hist = cv2.calcHist([chan],[0],None,[256],[0,256])
    features.extend(hist)

    #plot the histogram
    plt.plot(hist,color = color)
    plt.xlim([0,256])

#here we are simply showing the dimensionality of the
#flattened color histogram_256 bins for each channnel
#x 3 channels = 768 total values --- in practice, we would
#normally not use 256 bins for each channel, a choice
#between 32-96 bins are normally use ,
##but this is application dependent
print "flattened feature vector size: %d" %(np.array(features).flatten().shape)
#let's move on to 2-D histogram ---I am reducing the
#number of bins in histogram from 256 to 32 so we
#can better visualize the results

fig = plt.figure()

#plot a 2D color histogram for green and blue
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1],chans[0]],[0,1],None, [32,32],[0,256,0,256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D color Histogram for Green and Red")
plt.colorbar(p)

#finally , let's examine the dimensionality of one of
#the 2D histogram

print "2D histogaram shape : %s, with %d values" %(
    hist.shape, hist.flatten().shape[0])





# our 2D histogram could only take into account 2 out
# of the 3 channels in the image so now let's build a
# 3D color histogram (utilizing all channels) with 8 bins
# in each direction -- we can't plot the 3D histogram, but
# the theory is exactly like that of a 2D histogram, so
# we'll just show the shape of the histogram
hist = cv2.calcHist([img], [0, 1, 2],
	None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print "3D histogram shape: %s, with %d values" % (
	hist.shape, hist.flatten().shape[0])

plt.show()
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()

cv2.destroyAllWindows()
