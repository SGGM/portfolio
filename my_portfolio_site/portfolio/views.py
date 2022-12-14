from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def posts(request):
    return render(request, 'portfolio/posts.html')

def post(request):
    return render(request, 'portfolio/post.html')

def profile(request):
    return render(request, 'portfolio/profile.html')