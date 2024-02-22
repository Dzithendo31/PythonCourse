library = [
    {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
    {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
    {"title": "Advance Python", "author": "Mark Lutz", "year": 2015, "available": False},
]
def checkOutBook(library, title):
  for book in library:
    if (book['title'] == title and book['available']):
      #chnage availiability
      book['available'] = False
      return f"Availible book:{book['title']}"
    elif (book['title'] == title and not(book['available'])):
      return f"Book {book['title']}not in Stock"
    else: f'Book Not availible'

#Dictionaries are iterables