from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import recommend_movies, call_model
from rest_framework import routers


urlpatterns=[
    
    url(r'home/',views.home,name='home'),
    url(r'contact/',views.contact_us,name='contact_us'),
    url(r'profile/',views.profile,name='profile'),
    url(r'login/',LoginView.as_view(template_name='login.html'),name="login"),
    url(r'logout/',LogoutView.as_view(next_page='home'),name="logout"),
    url(r'^register/$',views.register,name='register'),
    url(r'^recommendations/$',views.home,name='show_movies'),
    path('r-api/recommend_movies/',recommend_movies.as_view()),
    url(r'nr-api/recommend_movies/',call_model.as_view()),
]