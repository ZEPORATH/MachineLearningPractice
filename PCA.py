from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle
import numpy as np


iris = load_iris()
#print iris.data.shape
numSamples, numFeatures = iris.data.shape
print numSamples
print numFeatures
print list(iris.target_names)

#Converting the 4D data features to 2D datafeatures
X = iris.data
pca = PCA(n_components =2,whiten=True).fit(X)
X_pca = pca.transform(X)

print "X_pca: ",X_pca
print "PCA Components: ", pca.components_

print "explained_variance_ratio_: ",pca.explained_variance_ratio_
print "Sum of explained_variance_ratio_:",sum(pca.explained_variance_ratio_)
print "explained_variance_: ",pca.explained_variance_


#Represent the data for plotting
colors = cycle('rgb')
target_ids = range(len(iris.target_names))
pl.figure()
for i,c,label in zip(target_ids, colors,iris.target_names):
    pl.scatter(X_pca[iris.target==i,0],X_pca[iris.target==i,1],c=c, label=label)
    
pl.legend()
pl.show()    
