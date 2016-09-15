import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
print pd.__version__

df=pd.read_excel('data/HHM-V6.xlsx','HHS appliances time of use W',index_col=None)


#df.rename(columns = {df.columns[0]:'House_no'}, inplace=True)
#print df.head(5)
House_ = pd.DataFrame(df[1:])
'''
for colname,col in df.iteritems():
    p=plt.figure()
    plt.scatter(df['House_no'],df[colname])
    plt.show(p)

X = df.iloc[1,:]
print X
devices = list(X.values)
print devices

Y = list(np.arange(0,25,1))
print Y
#   x = np.arange(X)

plt.scatter(X,Y)
plt.show()
'''
col_names = list(df.columns[1:])
columns_ = []
#print type(col_names), col_names
for i in col_names:
    x = str(i).replace("u'","")
    columns_.append(x)
print columns_

data = list(df.iloc[1,1:])
data_=[]
for i in data:
    x = int(i)
    data_.append(x)
print data_
'''
print type(data), data
df1 = pd.DataFrame(data,columns = (col_names),index = ['House1'])
print df1.head()

'''
d = {'columns': columns_,
     'data':[data_] ,
     'index': [1]}
df1 = pd.DataFrame(d['data'], columns=d['columns'], index=d['index'])
print df1
y= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
#ax = df1[df1.columns].plot(kind='bar', title ="V comp",figsize=(15,10),legend=True, fontsize=12)
df1.columns.names = ['SAMPLE']
df1.iloc[0].plot(kind = 'bar')
plt.show()

