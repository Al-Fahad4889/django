from django.shortcuts import render

def hello_django(request):
    return render(request, 'hello.html')
