from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns=[
    
    url(r'home/',views.home,name='home'),
    url(r'profile/',views.profile,name='profile'),
    url(r'login/',LoginView.as_view(template_name='login.html'),name="login"),
    url(r'logout/',LogoutView.as_view(next_page='home'),name="logout"),
    url(r'^register/$',views.register,name='register'),
]