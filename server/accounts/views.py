from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse  
from .serializers import UserSerializer
from .models import User
import jwt
import json
import requests
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def kakaoLoginView(request):
    print('겟')
    print()
    print()
    access_token = request.data['res']['access_token']
    url = 'https://kapi.kakao.com/v2/user/me'    
    headers = {
        'Authorization' : f'Bearer {access_token}',
        'Content-type' : 'application/x-www-form-urlencoded; charset=utf-8'
    }

    kakao_response = requests.get(url, headers=headers)
    kakao_response = json.loads(kakao_response.text)
    print(kakao_response)

    print('호잇')
    # kakao_id 로 검색해보고, 
    user = User.objects.filter(id=kakao_response['id'])
    print('됨')
    print(user.values())
    print()
    if user:
        # 있으면 로그인 진행
        print('있음 -> 로그인 진행')
        serializer = UserSerializer(instance=user[0])
        data = {
            'serializer' : serializer.data,
            'access' : access_token
        }
        res = Response(data, status=status.HTTP_200_OK)
        # print('res', res)
        # res.set_cookie(key='jwt', value=access_token, httponly=False)
        # res.set_cookie('access', access_token)
        # res.set_cookie('refresh', request.data['res']['refresh_token'])
        return res


    # 없으면 회원가입 진행
    print('없음 -> 회원가입 진행')
    
    user_data = {
        'id':kakao_response['id'],
        'username':kakao_response['properties']['nickname'],
        'email':kakao_response['kakao_account']['email'],
        'password':str(kakao_response['id']),
    }
    
    serializer = UserSerializer(data=user_data)

    if serializer.is_valid(raise_exception=True):
        print('들어옴')
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



@api_view(['GET'])
def mypage(request):
    print('마이페이지in')
    if request.user.is_authenticated:
        print('is_authenticated')
        if request.method == 'GET':
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)
    else:
        print('is_authenticated x')
        return Response(status=status.HTTP_401_UNAUTHORIZED)

