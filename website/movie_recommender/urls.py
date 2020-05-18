from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import recommend_movies, MoviesViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register('',MoviesViewSet)

urlpatterns=[
    
    url(r'home/',views.home,name='home'),
    url(r'profile/',views.profile,name='profile'),
    url(r'login/',LoginView.as_view(template_name='login.html'),name="login"),
    url(r'logout/',LogoutView.as_view(next_page='home'),name="logout"),
    url(r'^register/$',views.register,name='register'),
    url(r'^recommendations/$',views.home,name='show_movies'),
    path('api1/recommend_movies/',recommend_movies.as_view()),
    path('api2/recommend_movies/',include(router.urls)),
    url(r'^recommend_movies/',views.recommend_movies,name='movies'),
]