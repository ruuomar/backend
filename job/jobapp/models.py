from django.db import models
from datetime import date

# Create your models here.
class Job(models.Model):
    JId =models.AutoField(primary_key=True)
    JName=models.CharField(max_length=40)
    class Meta:
             db_table = 'job'

class Applicant(models.Model):
    AId =models.AutoField(primary_key=True)
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
       class Meta:
              db_table='apps'
