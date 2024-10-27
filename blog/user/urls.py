
from django.urls import path 
from django.contrib.auth import views as auth_views
from django.shortcuts import render 
from books.views import my_view, MyView, BookListView, ContactFormView 
from . import views
 
 
urlpatterns = [ 
    path('login/', auth_views.LoginView.as_view(template_name='login_view.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('sensitive-info/', views.sensitive_info_view, name='sensitive_info'),
]