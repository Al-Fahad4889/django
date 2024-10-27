from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, FormView
from books.models import Book
from django.urls import reverse_lazy
from books.forms import ContactForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer


# Create your views here.

def my_view(request):
    return HttpResponse("Welcome to Django!")

class MyView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django from class.")

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_success")  # Fixed this line

    def form_valid(self, form) -> HttpResponse:
        # Do something with the form data if necessary
        return super().form_valid(form)

class BookListCreate(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
        

    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)