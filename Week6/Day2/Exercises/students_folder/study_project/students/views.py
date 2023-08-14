from django.shortcuts import render
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from rest_framework.response import Response

# Shell request for daily challenge doesn't work
class Student_list(APIView):
    # @APIView(['GET'])
    def get(self, request, *args, **kwargs):
        date_joined_param = request.query_params.get('date_joined')
        
        if date_joined_param:
            students = Student.objects.filter(date_joined=date_joined_param)
        else:
            students = Student.objects.all()

        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
        
        
        # student = Student.objects.all()
        # serializer = StudentSerializer(student, many=True)
        # return Response(serializer.data)
        
class Student_detail(APIView):
    def get(self, request, pk, *args, **kwargs):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student)
        return Response(data=serializer.data)
            # return Response("error 404: Student object not found") 
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk, *args, **kwargs):
        post = Student.objects.get(id=pk)
        post.delete()
        return Response({'status 204 message':f'Post id - {pk} DELETED'})
    
    
    
    # def put(self, request, pk, *args, **kwargs):
    #     report = Student.objects.get(id=pk)
    #     serializer = StudentSerializer(instance=report, data=request.data)
    
    #     if serializer.valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # def delete(self, request, pk, *args, **kwargs):
    #     post = Student.objects.get(id=pk)
    #     post.delete()
    #     return Response({'message':f'Post id - {pk} DELETED'})
    
    