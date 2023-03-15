
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all() 
    return render(request, 'movies/index.html', {'movies': movies})
   
    ''' 
    Movie.objects.filter(release_year= 1990)
    # SELECT * FROM movies_movie WHERE release_year = year
    Movie.objects.get(id = 1) '''
            
     # return HttpResponse("Hello Prof Edward Dean of Cyber Security")
   
      # output = ', '.join([m.title for m in movies])
     # SELECT * FROM movies_movie
      #return HttpResponse(output)