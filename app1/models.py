from django.db import models

class info(models.Model):
	uname = models.CharField(max_length=255)
	email = models.EmailField()
	fname = models.CharField(max_length=255)
	lname = models.CharField(max_length=255)
	pno = models.IntegerField()
	pd = models.CharField(max_length=255)
