from django.db import models
from django.contrib.auth.models import User

WEATHER_TYPES = (
    ('Sy', 'Sunny'),
    ('Cy', 'Cloudy'),
    ('Wy', 'Windy'),
    ('Ry', 'Rainy'),
    ('Sy', 'Stormy'),
)

# Create your models here.
class Report(models.Model):
    location = models.CharField(max_length=50, null=False)
    temperature = models.FloatField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    types = models.CharField(max_length=3, choices=WEATHER_TYPES)
    
class Forecaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50, blank=False)