from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, "about.html")
    #return HttpResponse("<h1>Info about my blog</h1>")

def homepage(request):
    return render(request, "homepage.html")
    #return HttpResponse("home")
