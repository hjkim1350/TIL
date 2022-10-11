from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    return redirect('articles:index')