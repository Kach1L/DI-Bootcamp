"""
URL configuration for basic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from basicapp.views import DepartmentAPIView, EmployeeAPIView, ProjectAPIView, TaskAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('departments/', DepartmentAPIView.as_view(), name='department-detail'),
    path('employees/', EmployeeAPIView.as_view(), name='employee-detail'),
    path('projects/', ProjectAPIView.as_view(), name='project-detail'),
    path('tasks/', TaskAPIView.as_view(), name='task-detail'),
]

