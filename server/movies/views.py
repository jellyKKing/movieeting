from random import choices
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer, KeywordSerializer
from .models import Movie, Keyword
import csv
import pandas as pd
import json
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



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


@api_view(['GET'])
def test(request):
    movies_json_to_csv()
    movies_similarity_genre_set()
    print('💛💛💛💛💛💛💛💛')
    print(request)
    print('💛💛💛💛💛💛💛💛')
    

def movies_similarity_genre_set():
    csv_url = os.getcwd() + "\movies\\fixtures\movies.csv"
    df = pd.read_csv(csv_url, encoding='utf-8')

    counter_vector = CountVectorizer(ngram_range=(1,3))
    c_vector_genres = counter_vector.fit_transform(df['genres'])
    print('💖💖💖💖')
    print(c_vector_genres.shape)
    print('💖💖💖💖')

    similarity_genre = cosine_similarity(c_vector_genres, c_vector_genres).argsort()[:, ::-1]
    print(similarity_genre.shape)
    print('💖💖💖💖')


def movies_json_to_csv():
    json_url = os.getcwd() + "\movies\\fixtures\movies.json"
    df = pd.read_json(json_url, encoding='utf-8')
    csv_url = os.getcwd() + "\movies\\fixtures\movies.csv"
    # field names  
    fields = ['title', 'original_title', 'release_date', 'vote_average', 'popularity', 'overview', 'backdrop_path', 'poster_path', 'genres', 'keywords', 'actors', 'directors', 'vote_average_naver', 'link_naver']  
        
    # data rows of csv file  
    rows = []
    print(len(df['fields']))
    for i in range(1000):
        data = []
        data.append(df['fields'][i]['title']) #
        data.append(df['fields'][i]['original_title']) #
        data.append(df['fields'][i]['release_date']) #
        data.append(df['fields'][i]['vote_average']) #
        data.append(df['fields'][i]['popularity'])
        data.append(df['fields'][i]['overview']) #
        data.append(df['fields'][i]['backdrop_path']) #
        data.append(df['fields'][i]['poster_path']) #
        data.append(df['fields'][i]['genres']) 
        data.append(df['fields'][i]['keywords']) #
        data.append(df['fields'][i]['actors'])
        data.append(df['fields'][i]['directors'])
        if df['fields'][i].get('vote_average_naver', False):
            data.append(df['fields'][i]['vote_average_naver'])
            data.append(df['fields'][i]['link_naver'])
        rows.append(data)

    with open(csv_url, 'w', newline='', encoding="utf-8-sig") as f: 
        # using csv.writer method from CSV package 
        write = csv.writer(f) 
        
        write.writerow(fields) 
        write.writerows(rows)

                
