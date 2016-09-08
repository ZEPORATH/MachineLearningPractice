import numpy as np
import pandas as pd
from sklearn import tree
from IPython.display import Image
from sklearn.externals.six import StringIO
import matplotlib.pyplot as plt
import pydot


input_file = 'D:/DataScience/PastHires.csv'
df = pd.read_csv(input_file, header =0)

#print df.head()

d = {'Y' :1, 'N':0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Interned'] = df['Interned'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
d2 = {'BS':0, 'MS':1, 'PhD':2}
df['Level of Education'] = df['Level of Education'].map(d2)

#print df.head()

features = list(df.columns[:6])
#print features

Y = df['Hired']
X = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

#To display thedecision tree

dot_data = StringIO()
tree.export_graphviz(clf,out_file = dot_data, feature_names = features)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
print type(graph),graph 
''''
GraphViz\'s executables not found' )
InvocationException: GraphViz's executables not found
'''
#Image(graph.create_png())

#Ensemble Learning:Using random forest

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators = 10)
clf = clf.fit(X,Y)

#Predict employement of an employed 10-year old veteran
print clf.predict([10,1,4,0,0,0])
#Predict employement of an unemployed 10-year veteran
print clf.predict([10,0,4,0,0,0])
