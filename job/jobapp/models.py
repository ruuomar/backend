from django.db import models
from datetime import date
from django.utils import timezone


# Create your models here.
class Job(models.Model):
    JId =models.AutoField(primary_key=True)
    JName=models.CharField(max_length=40)
    class Meta:
             db_table = 'job'

class Applicant(models.Model):
    Aid =models.AutoField(primary_key=True)
    AFName=models.CharField(max_length=40)
    ALName=models.CharField(max_length=30)
    Address=models.CharField(max_length=40)
    AMobilePhone=models.IntegerField(default=False)
    AEmail=models.CharField(max_length=40)
    ABirth_date=models.DateField()
    class Meta:
             db_table = 'applicant'

class Apps(models.Model):
       JId = models.ForeignKey(Job,on_delete=models.CASCADE)
       Aid = models.ForeignKey(Applicant, on_delete=models.CASCADE)
       name=models.CharField(max_length=40)
       email=models.CharField(max_length=40)
       skill=models.CharField(max_length=40)
       wadhamin=models.CharField(max_length=50)
       document=models.FileField(upload_to='certificates/')
       class Meta:
              db_table='apps'
