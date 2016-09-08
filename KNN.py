import pandas as pd
import numpy as np

r_cols =['user_id','movie_id','rating']
ratings = pd.read_csv('D:/DataScience/ml-100k/u.data',sep='\t', names=r_cols, usecols=range(3))
print ratings.head()

#Group everything by movie id
movieProperties = ratings.groupby('movie_id').agg({'rating':[np.size, np.mean]})
print movieProperties.head()

#Create a normalized no of movie ratings
movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedRatings = movieNumRatings.apply(lambda x: (x - np.min(x))/ (np.max(x) - np.min(x)))
print movieNormalizedRatings.head()

r_cols1 = ['movieID', 'name','geners']
movieDictTable = pd.read_csv('D:/DataScience/ml-100k/u.item',sep='|',names = r_cols1,names[2] = range(3))
print movieDictTable.head()
#extracting the xenere items from u.item
movieDict = []
with open(r'D:/DataScience/ml-100k/u.item') as f:
    temp=''
    for line in f:
        fields = line.rstrip('\n').split('|')
        movieId = int(fields[0])
        name = fields[1]
        geners = fields[5:25]
        geners = map(int, geners)
        movieDict[movieId] = (name,geners,movieNormalizedRatings.loc[movieId].get('size'),movieProperties.loc[movieId].rating.get('mean'))
        
print movieDict 