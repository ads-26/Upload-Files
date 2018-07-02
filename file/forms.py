from django import forms
from .models import File

class FileForm(forms.Form):
	file  = forms.FileField()
	container = forms.CharField(label='Container' , max_length=100)
	obj = forms.CharField(label='Object' , max_length=100)