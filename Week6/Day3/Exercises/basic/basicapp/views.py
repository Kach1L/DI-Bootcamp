from django.shortcuts import render
from .serializers import DepartmentSerializer, EmployeeSerializer, ProjectSerializer, TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Department, Employee, Project, Task
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .permissions import IsDepartmentAdmin, Is

from rest_framework.views import APIView
from rest_framework.response import Response

class DepartmentAPIView(APIView):
    
    permission_classes = [IsDepartmentAdmin]
    
    def get(self, request, *args, **kwargs):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(data=serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = DepartmentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def put(self, request, pk, *args, **kwargs):
        departments = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(instance=departments, data=request.data)
    
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        departments = Department.objects.get(id=pk)
        
        self.check_object_permissions(request, departments)
        
        departments.delete()
        return Response({'message':f'Department id - {pk} DELETED'})
    
    

class EmployeeAPIView(APIView):
    
    permission_classes = [IsDepartmentAdmin]
    
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        serializer = DepartmentSerializer(employees, many=True)
        return Response(data=serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def put(self, request, pk, *args, **kwargs):
        employees = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(instance=employees, data=request.data)
    
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        employees = Employee.objects.get(id=pk)
        
        self.check_object_permissions(request, employees)
        
        employees.delete()
        return Response({'message':f'Employee id - {pk} DELETED'})
    
    

class ProjectAPIView(APIView):
    
    permission_classes = [IsDepartmentAdmin]
    
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = DepartmentSerializer(projects, many=True)
        return Response(data=serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def put(self, request, pk, *args, **kwargs):
        projects = Project.objects.get(id=pk)
        serializer = DepartmentSerializer(instance=projects, data=request.data)
    
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        projects = Project.objects.get(id=pk)
        
        self.check_object_permissions(request, projects)
        
        projects.delete()
        return Response({'message':f'Project id - {pk} DELETED'})
    
    
    
class TaskAPIView(APIView):
    
    permission_classes = [IsDepartmentAdmin]
    
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = DepartmentSerializer(tasks, many=True)
        return Response(data=serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def put(self, request, pk, *args, **kwargs):
        tasks = Task.objects.get(id=pk)
        serializer = DepartmentSerializer(instance=tasks, data=request.data)
    
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        tasks = Task.objects.get(id=pk)
        
        self.check_object_permissions(request, tasks)
        
        tasks.delete()
        return Response({'message':f'Task id - {pk} DELETED'})