from dataclasses import fields
from pyexpat import model
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Movie

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from rest_framework import serializers, viewsets

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hola Mundo desde templates</h1>')

def about(request):
    return HttpResponse('About')

def movies_index(request):
    movies = Movie.objects.all() # select * from api_movies


    return render(request, "movies/index.html", {'abc':"Hola Mundo", 'movies': movies})

def movies_create(request):
    return render(request, 'movies/create.html')

def movies_store(request):
    print(request.POST)
    print(request.FILES)

    if 'image' in request.FILES:

        image = request.FILES['image']

        path = default_storage.save("posters/" + image.name, ContentFile(image.read()))

        print(path)
    # movie = Movie()
    # movie.name = request.POST["titulo"]
    # movie.save()

    return redirect("movie_index")

def movies_json(request):
    movies = Movie.objects.select_related('gender').all()

    json_movies = []
    for o in movies:
        movie = {
            "id": o.id,
            "title": o.name,
            "gender": o.gender.name if o.gender else '-'
        }
        json_movies.append(movie)

    return JsonResponse(json_movies, safe=False)

#Permite serializar un objeto, en términos simples transforma un objeto complejo a texto
class MovieSerializer(serializers.ModelSerializer):

    gender_name = serializers.SerializerMethodField()
    players = serializers.SerializerMethodField()

    # for x in players:

    def get_gender_name(self, obj):
        return obj.gender.name if obj.gender else None
    
    def get_players(self, obj):
        return [x.name for x in obj.players.all()]

    class Meta:
        model = Movie
        fields = ['id', 'name', 'poster', 'gender_name', 'players']

#Coonfigura los metodos para, leer, crear, editar, eliminar
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related('gender').all()
    serializer_class = MovieSerializer