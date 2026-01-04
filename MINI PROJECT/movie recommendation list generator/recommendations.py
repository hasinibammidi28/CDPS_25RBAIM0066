# recommendations.py

from movies import movies

def recommend_by_genre(genre):
    return [movie for movie in movies if movie["genre"].lower() == genre.lower()]

def search_movie(title):
    return [movie for movie in movies if title.lower() in movie["title"].lower()]