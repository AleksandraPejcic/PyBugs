from django.contrib.auth.models import User
from django import forms
from django.db import models
from models import Projects,Bugs
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class AutoForm(forms.Form):
    
    projects_name = forms.ModelChoiceField(queryset=Projects.objects.all())
   
    class Meta:
        model = Projects
        fields = ('project_name')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects

class BugForm(forms.ModelForm):
    class Meta:
        model = Bugs

class DeveloperForm(forms.ModelForm): 
    class Meta:
        model = Bugs
        fields = ('developers',)

