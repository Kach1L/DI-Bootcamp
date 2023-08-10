from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    
class Author(models.Model):
    name = models.CharField(max_length=50) # By default, null values for the field.
    email = models.EmailField(blank=True, null=True)
        # blank = don't have to provide value for the field.
        # null - by default, null values are not allowed
        
# Shell commands

# to access the parent's model connected instances
# bill.post_set.all() <- get all posts of Bill
# bill.post_set.get(title='First Post') <- get the 'First Post' post of all 
    
