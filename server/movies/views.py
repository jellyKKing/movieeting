from random import choices
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer, KeywordSerializer, CommentSerializer
from .models import Movie, Keyword, Comment

from django.contrib.auth import get_user_model



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

        User = get_user_model()
        for i in range(len(serializer.data['comments'])):
            user = User.objects.filter(id=serializer.data['comments'][i]['user']).values()
            serializer.data['comments'][i]['username'] = user[0]['username']
            
        return Response(serializer.data)

@api_view(['GET'])
def popular(request):
    movie = Movie.objects.order_by('-popularity')[:11]
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def keyword(request, keyword_id):
    keyword = Keyword.objects.get(id=keyword_id)
    serializer = KeywordSerializer(keyword)
    return Response(serializer.data)

def findSimilarity():
    pass

# 좋아요
@api_view(['POST'])
def likes(request, movie_id):
    print('좋아요 django 입성')
    print(movie_id)
    print('')
    print(request.user)
    # 로그인한 사람만 좋아요~
    if request.user.is_authenticated:
        print('유저 들어옴')
        print('user.is_authenticated')
        movie = Movie.objects.get(pk=movie_id)

        # 좋아요 추가할지 취소할지 무슨 기준으로 if 문을 작성할까?
        # 2. 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지를 확인.
        # if request.user in article.like_users.all():
        # 1. 현재 게시글에 좋아요를 누른 유저중에 현재 좋아요를 요청하는 유저를 검색해서 존재하는지를 확인.
        if movie.like_users.filter(pk=request.user.pk).exists():
        # filter는 쓰고 get은 쓰지 않는 이유: get은 없으면 오류를 반환해서 코드가 진행이 안된다.
            # 좋아요 취소 (remove)
            movie.like_users.remove(request.user)
        else:
            # 좋아요 추가 (add)
            movie.like_users.add(request.user)
    movies = list(Movie.objects.filter(pk=movie_id).values())
    return Response(movies)
    
@api_view(['POST'])
def comment_create(request, movie_id):
    print('###테스트')
    # movie = Movie.objects.get(pk=movie_id)
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    # user = get_object_or_404(get_user_model(), pk=request.data['user_id'])
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)    # commit=False 대신에 외래키를 받기 위해서 article을 인자로 넣어준다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)
