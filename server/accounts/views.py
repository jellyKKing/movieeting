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
    user = User.objects.get(id=kakao_response['id'])

    if user:
        # 있으면 로그인 진행
        print('있음 -> 로그인 진행')
        serializer = UserSerializer(instance=user)
        res = Response(serializer.data, status=status.HTTP_200_OK)
        res.set_cookie('access', access_token)
        res.set_cookie('refresh', request.data['res']['refresh_token'])
        return res


    # 없으면 회원가입 진행
    print('없음 -> 회원가입 진행')
    
    user_data = {
        'id':kakao_response['id'],
        'password':kakao_response['id'],
        'username':kakao_response['properties']['nickname'],
        'email':kakao_response['kakao_account']['email'],
    }
    serializer = UserSerializer(data=user_data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        result = Response(serializer.data, status=status.HTTP_201_CREATED)
        result.set_cookie('access', access_token)
        result.set_cookie('refresh', request.data['res']['refresh_token'])
        return result
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

