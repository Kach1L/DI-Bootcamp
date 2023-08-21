from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, Teacher, SchoolFacility, Laboratory
from .serializers import TeacherSerializer, SchoolFacilitySerializer, LaboratorySerializer

class CourseDetails(APIView):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        data = {
            'course_name': course.course_name,
            'course_code': course.course_code
        }
        return Response(data)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

class SchoolFacilityListView(APIView):
    def get(self, request):
        facilities = SchoolFacility.objects.all()
        serializer = SchoolFacilitySerializer(facilities, many=True)
        return Response(serializer.data)

class LaboratoryListView(APIView):
    def get(self, request):
        laboratories = Laboratory.objects.all()
        serializer = LaboratorySerializer(laboratories, many=True)
        return Response(serializer.data)

