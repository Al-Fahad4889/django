from django.urls import path 
from django.contrib.auth import views as auth_views
from django.shortcuts import render 
from books.views import my_view, MyView, BookListView, ContactFormView 
 
 
urlpatterns = [ 
    path("initial/", my_view), 
    path("initial_class/", MyView.as_view()), 
    path("list/", BookListView.as_view()), 
    path("contact/add", ContactFormView.as_view()), 
    path("contact_success/", lambda request: render(request, "success/contact_success.html"), name="contact_success"), 
    path("book_form/", lambda request: render(request, "success/book_form.html"), name="book_form"),
    path('login/', auth_views.LoginView.as_view(template_name='login_view.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]