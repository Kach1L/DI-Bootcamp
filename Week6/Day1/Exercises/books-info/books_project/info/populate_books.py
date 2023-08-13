import requests
from info.models import Book  # Replace 'myapp' with the name of your app
from django.core.exceptions import ObjectDoesNotExist

# Define the search terms
search_terms = 'python programming'

# Send a GET request to the Google Books API
response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={search_terms}')
data = response.json()

# Parse the data and create Book objects
for item in data.get('items', []):
    volume_info = item.get('volumeInfo', {})
    title = volume_info.get('title')
    authors = volume_info.get('authors', [])
    
    # Check if the book already exists (based on title)
    try:
        existing_book = Book.objects.get(title=title)
    except ObjectDoesNotExist:
        # Create a new Book object
        new_book = Book(title=title, author=', '.join(authors))
        new_book.save()
        print(f"Created book: {title} by {', '.join(authors)}")
    else:
        print(f"Book already exists: {title} by {', '.join(authors)}")
