from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Book

# Create your views here.
def list_books(request):#list_books() works but instance needs to be created in the shell.
    all_books = list(Book.objects.all())
    return JsonResponse(all_books,safe=False)

def book_detail(request,id:int=0):#Same as list_books⬆️
    one_book = Book.objects.get(id=id)
    return JsonResponse(f'A Book: {one_book}')

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            title = data.get('title')
            author = data.get('author')
            if not title or not author:
                return JsonResponse({'error': 'Both title and author are required.'}, status=400)
            
            new_book = Book.objects.create(title=title, author=author)
            
            return JsonResponse({'message': 'Book created successfully', 'data': {
                'id': new_book.id,
                'title': new_book.title,
                'author': new_book.author,
                # Add other relevant fields here
            }})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
