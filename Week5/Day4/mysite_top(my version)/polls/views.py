from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author

# Create your views here.
def index(request):
    message = "Hello, this is my first page\n"
    return HttpResponse(message)

def about(request):
    text = """<h1>BLABLABLA<\h1>\n"""*100
    return HttpResponse(text)

def all_posts(request, author_name:str):
    try:
        author = Author.objects.get(name=author_name)
        author_posts = author.post_set.all()
        
        content = ""
        
        for post in author_posts:
            content += post.title + '\n'        
        
        return HttpResponse(content)
    except Author.DoesNotExist:
        return HttpResponse("""<h1>No such author""")
     