from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm':searchTerm})

def about(request):
    return render(request, 'about.html')