from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home/index.html")
def nav(request):
    return render(request, "partial/nav.html")