from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
from django.shortcuts import get_object_or_404

@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name and email:
            new_profile = Profile.objects.create(name=name, email=email)
            return JsonResponse({'message': 'Profile created successfully'})
        else:
            return JsonResponse({'error': 'Both name and email are required.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

@csrf_exempt
def delete_profile(request, id):
    if request.method == 'POST':
        profile = get_object_or_404(Profile, id=id)
        profile.delete()
        return JsonResponse({'message': 'Profile deleted successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
