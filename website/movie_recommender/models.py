from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact_Us(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	email=models.EmailField(max_length=70,blank=True)
	subject=models.CharField(default='',max_length=50)
	message=models.TextField(max_length=500)


class Movies_list(models.Model):
	Rating_choices=(
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
		)
	movie1=models.CharField(max_length=40)
	rating1=models.IntegerField(choices=Rating_choices,null=True,blank=True)
	movie2=models.CharField(max_length=40,null=True,blank=True)
	rating2=models.IntegerField(choices=Rating_choices,null=True,blank=True)
	movie3=models.CharField(max_length=40,null=True,blank=True)
	rating3=models.IntegerField(choices=Rating_choices,null=True,blank=True)
	movie4=models.CharField(max_length=40,null=True,blank=True)
	rating4=models.IntegerField(choices=Rating_choices,null=True,blank=True)
	movie5=models.CharField(max_length=40,null=True,blank=True)
	rating5=models.IntegerField(choices=Rating_choices,null=True,blank=True)

	def __str__(self):
		return self.movie1


	