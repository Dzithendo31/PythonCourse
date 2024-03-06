#HashMap -> key :Value
#Nested Dictionary

person = {
  "name" : "Siya Kolisi",
  "age" : 32,
  "address":{
    "city":"PE",
    "country":"SA",
    
  },
  "Stats":{
    "points":400
  },
  "height":186,
  "Sport":"Rugby"
}

print(person.get("address").get("city"))

#how do we
movie = {
  "name": "Mr Bones",
  "year": 2001
}

#making a copy
#1
movie_copy = movie.copy()
#2  using the upacking operator **
#unpack the Movie into a new dictionary
#you can add more keys to it
movie_Copy = {**movie, "rating":10}
print(movie_Copy)
#Just like that. becuase you can't have duplicate keys
movie_Copy2 = {**movie, "year":2002}
print(movie_Copy2)

detail = {
  "actor": "Quin",
  "Director": "Lin"
}

movie_dets = {**movie,**detail}
print(movie_dets)
