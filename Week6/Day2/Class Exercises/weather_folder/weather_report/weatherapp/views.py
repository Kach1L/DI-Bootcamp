from django.shortcuts import render
from .serializers import ReportSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Report
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .permissions import IsForecaster

from rest_framework.views import APIView
from rest_framework.response import Response

class ReportView(APIView):
    
    permission_classes = (IsForecaster,)
    
    def get(self, request, *args, **kwargs):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(data=serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ReportSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def put(self, request, pk, *args, **kwargs):
        report = Report.objects.get(id=pk)
        serializer = ReportSerializer(instance=report, data=request.data)
    
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        report = Report.objects.get(id=pk)
        
        self.check_object_permissions(request, report)
        
        report.delete()
        return Response({'message':f'Report id - {pk} DELETED'})
    
    