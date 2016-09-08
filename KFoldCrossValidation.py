import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
print iris.target

#print iris.data.shape
numSamples, numFeatures = iris.data.shape
print numSamples
print numFeatures
print list(iris.target_names)
'''
Using normal train test SVC model to predic iris species
As demonstrated in previous lectures too
'''
#Split the iris data into train/test data sets with 40% reserved for testing
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(iris.data,iris.target,test_size=0.4,random_state=0)
clf = svm.SVC(kernel='linear', C=1).fit(X_train,Y_train)

print clf.score(X_test,Y_test)

'''
Performing K-Fold cross validation of the data
'''
#we give cross_val_score a model, the entire data set and its "real" values
#and the number of folds

scores = cross_validation.cross_val_score(clf,iris.data,iris.target,cv=5)
print scores

#And the mean accuracy of the 5 folds
print scores.mean()

'''
Go ahead and try with a polynomial kernel
clf = svm.SVC(kernel='poly',C=1).fit(X_train, Y_train)
'''