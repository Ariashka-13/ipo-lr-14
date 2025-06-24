from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def author(request):
    return render(request, 'author.html')

def lamps(request):
    return render(request, 'lamps.html')