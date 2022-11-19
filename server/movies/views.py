from random import choices
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer
from .models import Movie



# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        random_movies = choices(movies, k=10)
        # print(movies[0])
        # serializer = MovieSerializer(movies, many=True)
        serializer = MovieSerializer(random_movies, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def detail(request, movie_id):
    if request.method == 'GET':
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie)
        # print(serializer.data)
        return Response(serializer.data)

@api_view(['GET'])
def popular(request):
    movie = Movie.objects.order_by('-popularity')[:11]
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)

def findSimilarity():
    pass