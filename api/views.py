from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Movie

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

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
    movies = Movie.objects.all()

    json_movies = []
    for o in movies:
        movie = {
            "id": o.id,
            "title": o.name   
        }
        json_movies.append(movie)

    return JsonResponse(json_movies, safe=False)
