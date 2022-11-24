from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.kakaoLoginView),
    path('mypage/', views.mypage),
    path('user/<int:user_id>/', views.userpage),
]