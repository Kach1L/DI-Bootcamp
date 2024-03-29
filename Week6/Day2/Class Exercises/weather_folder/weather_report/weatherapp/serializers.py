from rest_framework import serializers
from .models import Report, Forecaster

class ReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Report
        fields = ("location", "temperature", "created_at", "types")
        
class ForecasterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Forecaster
        fields = ("user", "name")