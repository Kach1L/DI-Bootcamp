from django.db import models

# Create your models here.
class Department(models.Model):
    projects = models.ManyToManyField('Project', related_name='departments')
    name = models.CharField(max_length=50, blank=False)
    date_founded = models.DateTimeField(auto_now_add=True)
    
class Employee(models.Model):
    departments = models.ManyToManyField('Department')  
    name = models.CharField(max_length=50, blank=False)
    date_hired = models.DateTimeField(auto_now_add=True)
    
class Project(models.Model):
    info = models.CharField(max_length=50, blank=False)
    date_started = models.DateTimeField(auto_now_add=True)
    
class Task(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    instruction = models.TextField(blank=False)
    date_assigned = models.DateTimeField(auto_now_add=True)
