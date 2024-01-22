from django.urls import path
from .import views
urlpatterns = [
    path('', views.home,name='home'),
    path('signUp/', views.signUp,name='signUp'),
    path('login/', views.LogIn,name='login'),
    path('logOut/', views.logOut,name='logOut'),
    path('pass_Change/', views.pass_Change,name='pass_Change'),
    path('profile/', views.profile,name='profile'),
    
]