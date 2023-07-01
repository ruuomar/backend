from django.shortcuts import render
from .models import Job
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from. models import Applicant, Job, Apps
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AppsSerializer

from django.core import serializers


# Create your views here.
# tuna create views ambayo inapeleka data kwenye database
@csrf_exempt
def insertJob(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        JId = data.get("JId")
        JName = data.get("JName")
        #then unasave kwajili kwenda kuziweka kwenye database
        job = Job(JId = JId,JName=JName)
        job.save()
        return JsonResponse({'massage':'Data Enter'})
    
@csrf_exempt    
def getJob(request):
    if request.method == 'GET':

        job = Job.objects.all()
        data = []
        for job in job:
            data.append({
                'JId':job.JId,
                'JName':job.JName
            })


        return JsonResponse(data, safe=False)
    
@csrf_exempt
def updateJob(request,JId):
    if request.method == 'PUT':
        job=Job.objects.get(JId=JId)
        data = json.loads(request.body)
        JName=data.get('JName')
        job.JName=JName
        job.save()
    return JsonResponse({job.JId:'updated'})

@csrf_exempt
def deleteJob(request,JId):
    if request.method == 'DELETE':
      job= Job.objects.get(JId=JId)
      job.delete()

      return JsonResponse({'data':'delete successifuly'})
  
@csrf_exempt
def insertApplicant(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        AId = data.get('AId') 
        AFName = data.get('AFName')
        ALName = data.get('ALName')
        Address = data.get('Address')
        AMobilePhone = data.get('AMobilePhone')
        AEmail = data.get('AEmail')
        ABirth_date = data.get('ABirth_date')
        applicant = Applicant(AId = AId,
                              AFName = AFName,
                              ALName = ALName,
                              Address= Address,
                              AMobilePhone = AMobilePhone,
                              AEmail = AEmail,
                              ABirth_date = ABirth_date)
        applicant.save()
    return JsonResponse({'massage':'Data Enter'})

# @csrf_exempt
# def getApplicant(request):
    # if request.method == 'GET':
    #     applicant = Applicant.objects.all()
    #     origin = request.META.get('HTTP_ORIGIN')
    #     data = []
    #     PendingDeprecationWarning
    #     for applicant in applicant:
    #         data.append({
    #         'AFName' : applicant.AFName,
    #         'ALName' :applicant. ALName,
    #         'Address':applicant.Address,
    #         'AMobilePhone' :applicant.AMobilePhone,
    #         'AEmail' :applicant.AEmail,
    #         'ABirth_date' :applicant.ABirth_date
        
    #     })
    #     return JsonResponse(data, safe=False)
@csrf_exempt
# @cors_exempt
def getApplicant(request):
    if request.method == 'GET':
        applicants = Applicant.objects.all()
        data = []
        sno = 1
        
        for applicant in applicants:
            data.append({
                'Sno': sno,
                'AFName': applicant.AFName,
                'ALName': applicant.ALName,
                'Address': applicant.Address,
                'AMobilePhone': applicant.AMobilePhone,
                'AEmail': applicant.AEmail,
                'ABirth_date': applicant.ABirth_date,
            })
            sno += 1
        
        return JsonResponse(data, safe=False)
    
@csrf_exempt
def updateApplicant(request,AId):
    if request.method  == 'PUT':
        applicant =Applicant.objects.all() 
        data =  json.loads(request.body)
        AFName=data.get('AFName')
        applicant.AFName=AFName
        ALName = data.get(ALName)
        applicant.ALName=ALName
        Address=data.get(Address)
        applicant.Address=Address
        AMobilePhone = data.get('AMobilePhone')
        applicant.AMobilePhone=AMobilePhone
        AEmail=data.get('AEmail')
        AEmail.AEmail=AEmail
        applicant.AMobilePhone=AMobilePhone
        ABirth_date = data.get(ABirth_date)
        applicant.ABirth_date=ABirth_date
        applicant.save()
        return JsonResponse({AId.AId:'updated'})
    
@csrf_exempt
def deleteapplicant(request,AId):
    if request.method == 'DELETE':
      applicant= Applicant.objects.get(AId=AId)
      applicant.delete()

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

        

        


