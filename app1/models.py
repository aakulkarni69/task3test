from django.db import models
from django.contrib.auth.models import User

class info(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	pno = models.IntegerField()

