from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    # category_set/categories (ManyToMany with Category)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)

        # blank - dont have to provide value for the field
        # null - by default, null values are not allowed

    # profile (OneToOne with Profile model)
    # post_set (OneToMany with Post model)

class Profile(models.Model):
    author = models.OneToOneField('Author', on_delete=models.CASCADE)
    image_url = models.URLField(blank=True, null=True)

class Category(models.Model): 
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField('Post', related_name='categories')

    def clean_name(self):
        if 'conspiracy' ==  self.name:
            raise ValidationError(f"Can't have conspiracy in category name")
        return self.name








# Shell commands

# to access the parent's (Author) model connected instances (Post)
# bill.post_set.all() <- get all posts of Bill
# bill.post_set.get(title='First Post') <- get the 'First Post' post of Bill

# To access the parent (Author) through the connected instance (Post)
# post1.author <- return an Author object of Bill 