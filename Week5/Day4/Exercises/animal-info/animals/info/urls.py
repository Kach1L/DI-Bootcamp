from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('/animals/', views.display_all_animals),
    path('/families/', views.display_all_families),
    path('/animal/', views.display_one_animal),
    path('/animalperfamily/', views.display_animal_per_family),
]