from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post

# Create your views here.
def index(request):
    message = "Hello, this is my first page"
    return HttpResponse(message)

def post(request, post_id:int):
    data = {
        1: "This is the 1st post",
        2: "This is the 2nd post"
    }
    post = data.get(post_id, "No such post")
    return HttpResponse(post)

def about(request):
    text = """<h1>BLABLABLA</h1>\n"""*100
    return HttpResponse(text)

# create a view that returns an HttpResponse
# with all of the posts of a certain Author
def all_posts(request, author_name:str):
    author_name = author_name.capitalize()
    try:
        author = Author.objects.get(name=author_name)
        author_posts = author.post_set.all()
        
        content = ""

        for post in author_posts:
            content += post.title + '\n'

        return HttpResponse(content)
    
    except Author.DoesNotExist:
        return HttpResponse("No such author")