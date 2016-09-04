import numpy as np
import random
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

def createClusterData(N,k):
    random.seed(10)
    pointsPerCluster = float(N)/k
    X = []
    for i in range (k):
        incomeCentroid = random.uniform(20000.0,200000.0)
        ageCentroid = random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([np.random.normal(incomeCentroid, 10000.0),np.random.normal(ageCentroid,2.0)])
    X = np.array(X)
    return X


data = createClusterData(100, 5)
model = KMeans(n_clusters =5)
#Scaling data to normalize it
model = model.fit(scale(data))

#look at the clusters generated
print model.labels_

#visualize the clusters
plt.figure(figsize=(8,6))
plt.scatter(data[:,0], data[:,1], c = model.labels_.astype(np.float))
plt.show()
plt.close()
