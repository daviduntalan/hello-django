from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse("<h1>Hello, World! ~ /home/david/my-projects/wsl-container-demo/hello-django/pages/views.py</h1>")
