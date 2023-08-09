from django.shortcuts import render
from django.http import HttpResponse

def display_person(request):
    name = 'Bob Smith'
    age = 35
    country = 'USA'
    
    content = f"Name: {name}\nAge: {age}\nCountry: {country}"
    return HttpResponse(content)

def display_people(request):
    people = ['bob', 'martha', 'fabio', 'john']
    people.sort()
    capitalized_people = [person.capitalize() for person in people]
    
    content = "\n".join(capitalized_people)
    return HttpResponse(content)

def display_all_people(request):
    all_people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]
    
    sorted_people = sorted(all_people, key=lambda x: x['age'])
    
    content = "\n".join([f"Name: {person['name']}, Age: {person['age']}" for person in sorted_people])
    return HttpResponse(content)