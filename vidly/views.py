# main home page of application
#1. create home in views
#2. map to url in vidly
#3. add to templates folder

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
