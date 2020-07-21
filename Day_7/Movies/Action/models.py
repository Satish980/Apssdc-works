from django.db import models

# Create your models here.

class Studentform(models.Model):
	s_name = models.CharField(max_length=50)
	s_age  = models.IntegerField()
	s_roll = models.CharField(max_length=10)
	s_email = models.EmailField(max_length=100)
