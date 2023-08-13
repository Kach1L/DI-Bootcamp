from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=50, blank=False)
    published_date = models.DateTimeField(auto_now_add=True, blank=False)
    description = models.TextField(max_length=50, blank=False)
    page_count = models.IntegerField(default=0, null=False)
    categories = models.CharField(max_length=50, blank=False)
    thumbnail_url = models.URLField()
    
class BookReview(models.Model):
    the_associated_book = models.ForeignKey(Book,on_delete=models.CASCADE,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    rating = models.IntegerField(null=False,validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField(max_length=10,null=False)
