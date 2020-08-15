from django.db import models
from django.contrib.auth.models import User                                 #imported django's inbuilt User class

class Info(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)    #Linked our info class one to one to user class
	pno = models.IntegerField(null=False)                                   #added extra field




