from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('login', views.login, name='login' ),
    path('signup', views.signup, name='signup' ),
    path('shows/<str:movie_title>/', views.movie_detail, name='movie_detail'),
    path('watch/<str:content_type>/<str:movie_title>/', views.watch, name='watch'),
    path('serie/watch/<str:movie_title>/<int:season_pk>/',
         views.serie_watch_page, name='serie_watch_page'),
]