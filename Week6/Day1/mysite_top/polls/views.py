from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post, Category

# Create your views here.
def index(request):
    message = "Hello, this is my first page"
    return HttpResponse(message)

def post(request, post_id:int):
    try:
        post = Post.objects.get(id = post_id)
        content = f"AUTHOR:{post.author.name} | TITLE: {post.title} | Text:{post.text}"
        return HttpResponse(content)
    except Post.DoesNotExist:
        return HttpResponse("No such post")
    
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
    
# create a view that accepts id of a category and returns an HttpResonse with all of the posts of that category
# add a url endpoint 
def category_posts(request, category_id:int):
    try:
        category = Category.objects.get(id=category_id)
        posts = category.posts.all()
        content = ""
        for post in posts:
            content += f'{post.title} - {post.author.name}</br>'
        return HttpResponse(content)
    except Category.DoesNotExist:
        return HttpResponse("No such category")
