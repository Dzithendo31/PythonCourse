#Don't use loops and
#Addd the Average rating

movies = [
  {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
  {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
  {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
  {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
  {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
]

# Task 1 - Find average for all - map, filter, all, ...
# Dont use for loop or List comp
answer = map(lambda x: x['title'],movies)
print(list(answer))

def aver(x):
  return sum(x['ratings'])/len(x['ratings'])
#task 1.1
average = map(lambda x: aver(x), movies)
print(list(average))

#task 1.2
moves = map(lambda x: {"ave":aver(x)},movies)
moviez = map(lambda x,y:{**x,**y},movies,moves)
moviez = (list(moviez))

altMovies = map(
  lambda movie:{
    **movie,"ave":aver(movie)
  },movies)
print(list(altMovies))

#Task 2.0 Top rated movie
top_rated = max(moviez, key=lambda x:x['ave'])
print(top_rated['title'])


#Task 3.0
#No for loop
#Movies with more tha 4.5
topMovies = list(filter(lambda movie: movie['ave']>4.5,altMovies))
print(list(topMovies))
print(list(map(lambda movie: movie['title'],topMovies)))


#Task 4
#Sort based on rating
sortedMovies = sorted(altMovies,key=lambda x:x['ave'])
print(sortedMovies)
print(list(map(lambda movie: movie['title'],sortedMovies)))