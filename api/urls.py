from django.urls import path
from .views import index, about, movies_index, movies_create, movies_store, movies_json

urlpatterns = [
    path('hello', index),
    path('about', about),
    path('movies', movies_index, name="movie_index"),
    path('movies/create', movies_create),
    path('movies/store', movies_store),

    path('json/movies', movies_json),
]

#https://localhost:8080/api/{path}