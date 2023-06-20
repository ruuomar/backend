from django.shortcuts import render
from .models import Job
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

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
    
def data_view(request):
    data = Job.objects.all()
    return render(request, 'data.html', {'data': data})

