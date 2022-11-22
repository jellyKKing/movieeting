from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:movie_id>/', views.detail),
    path('popular/', views.popular),
    path('keyword/<int:keyword_id>/', views.keyword),
    path('<int:movie_id>/likes/',views.likes, name='likes'),
    path('<int:movie_id>/comments/',views.comment_create,),
]