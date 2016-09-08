import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('D:/DataScience/ml-100k/u.data',sep='\t', names = r_cols, usecols=range(3))

m_cols = ['movie_id', 'title']
movies = pd.read_csv('D:/DataScience/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2))

ratings = pd.merge(movies, ratings)

print ratings.head()

movieRatings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
print movieRatings.head()

starWarRatings = movieRatings['Star Wars (1977)']
print starWarRatings.head()

similarMovies = movieRatings.corrwith(starWarRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
print df.head()

print similarMovies.order(ascending=False)


