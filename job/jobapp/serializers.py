from rest_framework import serializers
from .models import Job,Applicant,Apps


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['JId','JName']

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['Aid','AFName','ALName','Address','AMobilePhone','AEmail','ABirth_date']                

class AppsSerializer(serializers.ModelSerializer):
    job =JobSerializer(source='JId',read_only=True)
    applicant = ApplicantSerializer(source='Aid',read_only=True)
    class Meta:
        model = Apps
        fields = ['id','JId','Aid','name','email','skill','wadhamin','job','applicant']

