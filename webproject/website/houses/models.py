from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Houses(models.Model):
	owner = models.CharField(max_length=250)
	house_name  = models.CharField(max_length=500)
	country = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	thumb = models.ImageField(default="default.png")
	body = models.TextField(default=None)
	def __str__(self):
		return self.house_name


class house(models.Model):
	houses = models.ForeignKey(Houses, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=10)
	house_name = models.CharField(max_length=250)


class post(models.Model):
	your_name = models.CharField(max_length=100)
	your_email = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	message = models.TextField(default=None)
	def __str__(self):
		return self.subject


