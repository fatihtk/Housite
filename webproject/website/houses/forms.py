from django import forms
from . import models


class CreateHouses(forms.ModelForm):
	class Meta:
		model = models.Houses
		fields = ['owner','house_name','country','genre','thumb','body']

class post(forms.ModelForm):
	class Meta:
		model = models.post
		fields = ['your_name','your_email','subject','message']

