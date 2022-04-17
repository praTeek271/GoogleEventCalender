from django.db import models

# Create your models here.
appid=1
class celenderEvent(models.Model):
 
    event_name=models.CharField(max_length=100,default=f'Appointment {appid}')
    appid+=1
    catogory=models.CharField(max_length=50)
    priorty=models.CharField(max_length=50)
    eventTYPE=models.CharField(max_length=50)