from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)