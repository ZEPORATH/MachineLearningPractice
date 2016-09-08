import numpy as np
import random
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

def createClusterData(N,k):
    random.seed(10)
    pointsPerCluster = float(N)/k
    X = []
    Y = []
    for i in range (k):
        incomeCentroid = random.uniform(20000.0,200000.0)
        ageCentroid = random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([np.random.normal(incomeCentroid, 10000.0),np.random.normal(ageCentroid,2.0)])
            Y.append(i)
    X = np.array(X)
    Y = np.array(Y)
    return X, Y

(X,Y) = createClusterData(100,5)

plt.figure(figsize = (8,6))
plt.scatter(X[:,0], X[:,1], c = Y.astype(np.float))
plt.show()
plt.close()

def plotPredictions(clf):
    xx, yy = np.meshgrid(np.arange(0,250000,10),np.arange(10,70,0.5))
    z = clf.predict(np.c_[xx.ravel(),yy.ravel()])

    plt.figure(figsize=(8,6))
    Z = z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap = plt.cm.Paired, alpha=0.8)
    plt.scatter(X[:,0], X[:,1], c=Y.astype(np.float))
    plt.show()

from sklearn import svm, datasets
c = 1.0
svc = svm.SVC(kernel='linear', C = c).fit(X,Y)
plotPredictions(svc)
