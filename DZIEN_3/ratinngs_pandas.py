import pandas as pd

unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('dane/users.dat',engine='python',sep="::",header=None,names=unames)

rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('dane/ratings.dat',engine='python',sep="::",header=None,names=rnames)

mnames = ['movie_id','title','genres']
movies = pd.read_table('dane/movies.dat',encoding='ISO-8859-1',engine='python',sep="::",header=None,names=mnames)


print(users[:5])
print("_"*60)
print(ratings[:5])
print("_"*60)
print(movies[:5])
print("_"*60)


data = pd.merge(pd.merge(ratings,users),movies)
print(data)

rt = ratings.merge(users,left_on="user_id",right_on="user_id")

print("_"*60)
print(rt[:10])

print("_"*60)

mean_ratings = data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')
print(mean_ratings[:10])

print("_"*60)


ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10])

print("_"*60)
active_titles = ratings_by_title.index[ratings_by_title>=250]
print(active_titles)

print("_"*60)
mean_ratings = mean_ratings.loc[active_titles]

print(mean_ratings[:10])

top_female_ratings = mean_ratings.sort_values(by='F',ascending=False)
print(top_female_ratings[:10])
