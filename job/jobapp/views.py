from django.shortcuts import render
from .models import Job
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from. models import Applicant, Job, Apps
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobSerializer,ApplicantSerializer,AppsSerializer

from django.core import serializers


# Create your views here.
# tuna create views ambayo inapeleka data kwenye database
# @csrf_exempt
# def insertJob(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         JId = data.get("JId")
#         JName = data.get("JName")
#         #then unasave kwajili kwenda kuziweka kwenye database
#         job = Job(JId = JId,JName=JName)
#         job.save()
#         return JsonResponse({'massage':'Data Enter'})

# for job
@api_view(['POST'])
def insertJob(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def getJobbyID(request,JId) :
    job =Job.objects.get(JId=JId)
    serializer=JobSerializer(job)
    return Response(serializer.data)

@api_view(['GET'])
def getJob(request) :
    job = Job.objects.all()
    serializer = JobSerializer(job,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def updateJob(request,JId):
    job = Job.objects.get(JId=JId)
    serializer=JobSerializer(job,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response (serializer.errors, status = 400)

@api_view(['DELETE'])
def deleteJob(request,JId):
    job = Job.objects.get(JId = JId)
    job.delete()
    return Response(status=204)   
   

#   For Applicant
@api_view(['POST'])
def insertApplicant(request):
    serializer = ApplicantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getApplicantbyID(request,Aid) :
    applicant =Applicant.objects.get(Aid=Aid)
    serializer=ApplicantSerializer(applicant)
    return Response(serializer.data)

@api_view(['GET'])
def getApplicant(request) :
    applicant = Applicant.objects.all()
    serializer = ApplicantSerializer(applicant,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def updateApplicant(request, Aid):
    try:
        applicant = Applicant.objects.get(Aid=Aid)
    except Applicant.DoesNotExist:
        return Response(status=404)
    
    serializer = ApplicantSerializer(applicant, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteapplicant(request, Aid):
    applicant = Applicant.objects.get(Aid = Aid)
    applicant.delete()
    return Response(status=204)   
       

# for foreign key
@api_view(['POST'])
def insertAppJob(request) :
    serializer = AppsSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
    return Response(serializer.errors,status=400)


@api_view(['GET'])
def getAppJob(request) :
    app = Apps.objects.all()
    serializer=AppsSerializer(app,many=True)
    return Response(serializer.data)

# kuchukuwa kwa kutumia  by id  
@api_view(['GET'])
def getbyid(request, id):
    app = Apps.objects.get(id=id)
    serializer=AppsSerializer(app)
    return Response(serializer.data)

@api_view(['PUT'])
def updateAppJob(request,id):
    app = Apps.objects.get(id=id)
    serializer=AppsSerializer(app,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response (serializer.errors, status = 400)

@api_view(['DELETE'])
def deleteAppJob(request,id):
    app = Apps.objects.get(id = id)
    app.delete()
    return Response(status=204)


# def upload_view(request):
#     if request.method == 'POST' and request.FILES.get('document'):
#         document = request.FILES['document']
#         # Implement your file handling logic here
#         # Validate the file, save it, and send a response back to the frontend
#         return render(request, 'upload.html', {'message': 'File uploaded successfully'})
    
#     return render(request, 'upload.html')

        

        


