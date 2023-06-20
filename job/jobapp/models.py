from django.db import models

# Create your models here.
class Job(models.Model):
    JId =models.AutoField(primary_key=True)
    JName=models.CharField(max_length=40)
    # JPost=models.CharField(max_length=20)
    class Meta:
             db_table = 'job'

class Applicant(models.Model):
    AId =models.AutoField(primary_key=True)
    AF_Name=models.CharField(max_length=40)
    AL_Name=models.CharField(max_length=30)
    AAddress=models.CharField(max_length=40)
    AMobilePhone=models.IntegerField(default=False)
    AEmail=models.CharField(max_length=40)
    ABirth_date=models.DateField()
    class Meta:
             db_table = 'applicant'

class AppJob(models.Model):
        JID=models.ForeignKey(Job, on_delete=models.CASCADE)
        AId=models.ForeignKey(Applicant, on_delete=models.CASCADE)
        class Meta:
             db_table = 'appjob'