#import the necessaary packages
import numpy as np
import matplotlib.pyplot as plt
from rgbhistogram import RGBHistogram
import argparse, cPickle, glob,cv2


#construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d","--dataset", required = True,
                help='Path to the directory that contains the images to be indexed')

ap.add_argument("-i","--index", required=True,
                help="PAth to where the computed index will be stored")
args = vars(ap.parse_args())

#initialize the index dictionary to store our quantified
#images, with the 'key' of the dictionary as image
#filename and the 'vale' oue computed features

index = {}

desc = RGBHistogram([8,8,8])

for imagePath in glob.glob(args["dataset"]+"/*.png"):
    k = imagePath[imagePath.rfind("/")+1:]

    #load the image , describe it using our RGB histogram
    #descriptr, and update the index
    image = cv2.imread(imagePath)
    features = desc.describe(image)
    index[k] = features

#we are now done indexing our image --now we can write our
#index to the disk
    
f = open(args["index"],"w")
f.write(cPickle.dumps(index))
f.close()

class Searcher:
    def __init__(self, index):
        self.index = index
        #store our index of images
        
    def search(self,QuerryFeatures):
        #initalize our dictionary of results
        results = {}

        #loop over the index
        for (k,features) in self.index.items():
            #compute the chi-squared distance between the features
            #in our index and querry features-- using the
            #chi-squared distance we just computed, representing
            #how 'similar' the image in the index is to our querry
            d = self.chi2_distance(feature,QuerryFeatures)

            #now that we have the distance between the two features
            #vectors, we can update the results in the result dictionary -- the
            #key is cutrrent image ID , in the index and
            #the value os the distance we just computed, representing
            #how similar the images in the index is tour querry
            results[k] = d

        ##sort out the results, so that the smaller distances i.e,
        ##more relevant images ae at the front of the list

        results = sorted([(v,k) for (k,v) in results.items()])

        return results

    def chi2_distance(self, histA, histB, eps= 1e-10):
        #compute the chi_squared distance
        d = 0.5*np.sum([((a-b)**2)/(a+b+eps) for (A,b) in zip(histA, hsitB)])

        return d


#load the index and initialize our searcher
index = cPickle.loads(open(args["index"]).read())
searcher = Searcher(index)

#loop over images in the index -- we will use each one as
#a querry image

for (query, querryFeatures) in index.items():
    #perform the search using the querry
    results = searcher.search(querryFeatures)

    #load the querry image and display it
    path = args["dataset"]+"/%s"%(query)
    queryImage = cv2.imread(path)
    cv2.imshow("Querry", queryImage)
    print "querry: %s" % (query)

    #initialize 2 montages to display our results --
    # we have a total of 25 images in the index, but let's only
    #display the top10 results: 5 images per montage, with
    #images that ase 400x166 pixels
    montageA = np.zeros((166*5,400,3), dtype = "uint8")
    montageB = np.zeros((166*5,400,3), dtype = "uint8")

    #loop over top ten results
    for j in xrange(0,10):
        #grab the result (we are using row-major order) and
        #load the results image
        (score, imageName) = results[j]
        path = args["dataset"]+"/%s" % (imageName)
        result - cv2.imread(path)
        print "\t%. %s: %3f" %(j+1, imageName, score)
        

# check to see if the first montage should be used
        if j<5:
            montage[j*166:(j+1)*166, :] = result
        #otherwise, the second montage should be used
        else:
            montageB[(j-5)*166:((j-5)+1)*166, :]= result

    #show the results
    cv2.imshow("Results 1-5", montageA)
    cv2.imshow("Results 6-10", montageB)

    cv2.waitkey(0)        
                
