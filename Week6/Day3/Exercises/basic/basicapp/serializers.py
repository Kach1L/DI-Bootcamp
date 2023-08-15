from rest_framework import serializers
from .models import Department, Employee, Project, Task

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='department-detail')  # Adjust the view name

    class Meta:
        model = Department
        fields = ['url', 'id', "projects", "name", "date_founded"]
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='employee-detail')  # Adjust the view name

    class Meta:
        model = Employee
        fields = ['url', 'id', "projects", "name", "date_founded"]
    
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project-detail')  # Adjust the view name

    class Meta:
        model = Project
        fields = ['url', 'id', "departments", "name", "date_hired"]
    
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')  # Adjust the view name

    class Meta:
        model = Task
        fields = ['url', 'id', "project", "instruction", "date_assigned"]
    