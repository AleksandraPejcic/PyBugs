from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User,Group

class Bugs(models.Model):

    summary = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=10000, blank=True)
    start_date = models.DateField(blank=True, null=True)
    project = models.ForeignKey("Projects")
    developers = models.ManyToManyField("auth.User",unique=False,related_name = 'developers',limit_choices_to = {'groups__name' :Group.objects.get(name='developers').name})
    
    def natural_key(self):
        return (self.summary,self.status,self.description,self.start_date,self.project,self.developers)
    def __unicode__(self): # to display name of projects in drop down in BugField 
        return (self.summary,self.status,self.description,self.start_date,self.project,self.developers)

    class Meta:
        db_table = 'bugs'


class Projects(models.Model):
    
    name = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True, null=True)
    project_manager = models.ForeignKey("auth.User",unique=False,related_name = 'project_managers',limit_choices_to = {'groups__name' :Group.objects.get(name='project_managers').name})
    def natural_key(self):
        return (self.name)
    def __unicode__(self): # to display name of projects in drop down in BugField 
        return self.name

    class Meta:   
        db_table = 'projects'



    
class User(User):
    class Meta:
        permissions = (('can_delete', 'Can delete') ,
                       ('can_viewpage' 'Can view page'),
                      )       