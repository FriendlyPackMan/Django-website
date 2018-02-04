from django.http import HttpResponse

def about(request):
    return HttpResponse("<h1>Info about my blog</h1>")

def homepage(request):
    return HttpResponse("home")
