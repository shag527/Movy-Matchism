from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact_Us(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	email=models.EmailField(max_length=70,blank=True)
	subject=models.CharField(default='',max_length=50)
	message=models.TextField(max_length=500)
