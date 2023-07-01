from rest_framework import serializers
from .models import Job,Applicant,Apps

class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = ['id','JId','Aid']