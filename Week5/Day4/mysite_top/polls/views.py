from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    message = "Hello, this is my first page\n"
    return HttpResponse(message)

def about(request):
    text = """<h1>BLABLABLA<\h1>\n"""*100
    return HttpResponse(text)

# Create views.