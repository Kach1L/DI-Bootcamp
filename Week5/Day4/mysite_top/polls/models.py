from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
        # blank - dont have to provide value for the field
        # null - by default, null values are not allowed

# Shell commands

# to access the parent's (Author) model connected instances (Post)
# bill.post_set.all() <- get all posts of Bill
# bill.post_set.get(title='First Post') <- get the 'First Post' post of Bill

# To access the parent (Author) through the connected instance (Post)
# post1.author <- return an Author object of Bill 