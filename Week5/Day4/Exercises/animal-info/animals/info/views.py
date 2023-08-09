from django.shortcuts import render
from django.http import HttpResponse
from .data import animals, families

# Create your views here.
def display_all_animals(request):
    ani_list = []
    for animal in animals:
        animal_info = f"{animal['name']}, {animal['legs']}, {animal['weight']}, {animal['height']}, {animal['speed']}. "
        ani_list.append(animal_info)
    return HttpResponse(ani_list)

def display_all_families(request):
    ani_list1 = []
    for family in families:
        family_names = f"{family['name']} "
        ani_list1.append(family_names)
    return HttpResponse(ani_list1)

def display_one_animal(request, animal_id=2):
    one_animal = []
    animal_choice = f"{animals[animal_id]['name']}, {animals[animal_id]['legs']}, {animals[animal_id]['weight']}, {animals[animal_id]['height']}, {animals[animal_id]['speed']}, {animals[animal_id]['family']} "
    one_animal.append(animal_choice)
    return HttpResponse(one_animal)

def display_animal_per_family(request, family_id=1):
    one_animal = []
    if family_id == 0:
        animal_choice = f"{animals[family_id]['name']}, {animals[family_id]['legs']}, {animals[family_id]['weight']}, {animals[family_id]['height']}, {animals[family_id]['speed']}, {animals[family_id]['family']}. "
        one_animal.append(animal_choice)
    elif family_id == 1:
        animal_choice = f"{animals[family_id]['name']}, {animals[family_id]['legs']}, {animals[family_id]['weight']}, {animals[family_id]['height']}, {animals[family_id]['speed']}, {animals[family_id]['family']}. {animals[family_id+1]['name']}, {animals[family_id+1]['legs']}, {animals[family_id+1]['weight']}, {animals[family_id+1]['height']}, {animals[family_id+1]['speed']}, {animals[family_id+1]['family']} "
        # animal_choice2 = f"{animals[family_id+1]['name']}, {animals[family_id+1]['legs']}, {animals[family_id+1]['weight']}, {animals[family_id+1]['height']}, {animals[family_id+1]['speed']}, {animals[family_id+1]['family']}. "
        one_animal.append(animal_choice)
    
    # for a in animals:
    #     animal_choice = f"{animals[family_id]['name']}, {animals[family_id]['legs']}, {animals[family_id]['weight']}, {animals[family_id]['height']}, {animals[family_id]['speed']}, {animals[family_id]['family']} "
    # one_animal.append(animal_choice)
    return HttpResponse(one_animal)
    



