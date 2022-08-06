from django.urls import path, include
from .views import MovieViewSet, index, about, movies_index, movies_create, movies_store, movies_json
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
# router.register('books', BookViewSet) #ejemplo
# router.register('users', UserViewSet)

# http://dominio.com/api/movies -> GET -> all
# http://dominio.com/api/movies -> POST -> crear
# http://dominio.com/api/movies/1 -> GEt -> un elemento
# http://dominio.com/api/movies/1 -> PUT -> actualizar
# http://dominio.com/api/movies/1 -> DELETE -> eliminar

urlpatterns = [

    path('', include(router.urls)),

    path('hello', index),
    path('about', about),
    
    #path('movies', movies_index, name="movie_index"),
    #path('movies/create', movies_create),
    #path('movies/store', movies_store),

    path('json/movies', movies_json),
]

#https://localhost:8080/api/{path}