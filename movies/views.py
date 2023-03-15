
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all() 
    return render(request, 'movies/index.html', {'movies': movies})
   
   
def detail(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
        
   
      
        
    
    #return HttpResponse(movie_id)
   
   
   
   
    ''' 
    Movie.objects.filter(release_year= 1990)
    # SELECT * FROM movies_movie WHERE release_year = year
    Movie.objects.get(id = 1) '''
            
     # return HttpResponse("Hello Prof Edward Dean of Cyber Security")
   
      # output = ', '.join([m.title for m in movies])
     # SELECT * FROM movies_movie
      #return HttpResponse(output)