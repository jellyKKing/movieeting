from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse  
from .serializers import UserSerializer
from .models import User
from movies.models import Movie, Comment
import jwt
import json
import requests
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def kakaoLoginView(request):
    access_token = request.data['res']['access_token']
    url = 'https://kapi.kakao.com/v2/user/me'    
    headers = {
        'Authorization' : f'Bearer {access_token}',
        'Content-type' : 'application/x-www-form-urlencoded; charset=utf-8'
    }

    kakao_response = requests.get(url, headers=headers)
    kakao_response = json.loads(kakao_response.text)

    # kakao_id 로 검색해보고, 
    user = User.objects.filter(id=kakao_response['id'])
    if user:
        # 있으면 로그인 진행
        serializer = UserSerializer(instance=user[0])
        data = {
            'serializer' : serializer.data,
            'access' : access_token
        }
        res = Response(data, status=status.HTTP_200_OK)
        return res


    # 없으면 회원가입 진행
    print('없음 -> 회원가입 진행')
    
    user_data = {
        'id':kakao_response['id'],
        'username':kakao_response['properties']['nickname'],
        'email':kakao_response['kakao_account']['email'],
        'password':str(kakao_response['id']),
        'gender':kakao_response['kakao_account']['gender'],
        'imgUrl':kakao_response['kakao_account']['profile']['profile_image_url'],
    }
    
    serializer = UserSerializer(data=user_data)

    if serializer.is_valid(raise_exception=True):
        users = serializer.save()
        password = str(kakao_response['id'])
        users.set_password(password)
        users.save()
        data = {
            'serializer' : serializer.data,
            'access' : access_token
        }
        result = Response(data, status=status.HTTP_201_CREATED)
        return result
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def mypage(request):
    print('마이페이지in')
    
    if request.user.is_authenticated:
        print('is_authenticated')
        print()

        # 사용자가 좋아요 누른 영화 목록
        movies = User.objects.filter(id=request.user.id)[0].like_movies.all().values()

        # 사용자가 작성한 리뷰
        comments = Comment.objects.filter(user_id=request.user.id).values()

        # 사용자의 팔로워
        
        data = {
            'user_like_movies' : movies,
            'user_created_comments' : comments,
        }
        return Response(data)

    print('is_authenticated x')
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def userpage(request, user_id):
    print('userPage in 💛')
    print(user_id)
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(instance=user)

    # 사용자가 좋아요 누른 영화 목록
    movies = User.objects.filter(id=user_id)[0].like_movies.all().values()

    # 사용자가 작성한 리뷰
    comments = Comment.objects.filter(user_id=user_id).values()

    serializer.data['user_like_movies'] = movies
    serializer.data['user_created_comments'] = comments

    return Response(serializer.data)
