from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:movie_id>/', views.detail),
    path('popular/', views.popular),
    path('keyword/<int:keyword_id>/', views.keyword),
]