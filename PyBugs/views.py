from django.shortcuts import render
from forms import UserForm,AutoForm,ProjectForm,BugForm,DeveloperForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from PyBugs.models import Projects,Bugs
import models
import json
from django.contrib.auth.models import User,Group
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):

    return render(request ,'PyBugs/index.html')

def account(request):
    return render(request ,'PyBugs/account.html')

def login(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                    auth_login(request, user)
                    # Redirect to a success page.
                    return HttpResponseRedirect('/account/')                
            else:
                state ="Your account is not active, please contact the site admin."
        else:
          state = "Your username and/or password were incorrect."
    return render(request ,'PyBugs/index.html',{'username': username,})




def logout(request):
    auth.logout(request)
    return HttpResponseRedirect ('/index/')  

def account(request):
    latest_Project_list = Projects.objects.all().order_by('id')[:50] 
    latest_bugs_list = Bugs.objects.all().order_by('id')[:50]
    context = {'latest_bugs_list':latest_bugs_list ,'latest_Project_list':latest_Project_list }
    return render(request, 'PyBugs/account.html', context)


def bugs_table(request,pk):
    project=Projects.objects.select_related().get(id=pk)
    bugs = Bugs.objects.filter(project_id=project)
    leads_as_json=serializers.serialize('json', bugs ,indent = 4, use_natural_keys=True)
    print leads_as_json
    return HttpResponse(leads_as_json, content_type='json')

def new_bug(request):

    
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():     
            form.save()       
            # Redirect to a success page. 
            return HttpResponseRedirect('/account/') 
    else:
        form=BugForm()    
    return render(request, 'PyBugs/new_bug.html', {'form': form,})        


def create_project(request):

    if request.method == 'POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()    
            return HttpResponseRedirect("/account/")
    else:
  
            form=ProjectForm()

    return  render(request, 'PyBugs/create_project.html', {'form': form,}) 

def create_developer(request):

    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            user=form.save()   
            user.groups.add(Group.objects.get(name='developers')) 
            return HttpResponseRedirect("/account/")
    else:
            form=UserForm()
    return  render(request, 'PyBugs/new_developer.html', {'form': form,})

def edit_developer(request,pk):
    if request.method == 'POST':
        b=Bugs.objects.get(pk=pk)
        form = DeveloperForm(request.POST,instance = b)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/account/') 
    else:
            form=DeveloperForm()
    return render(request, 'PyBugs/edit_developer.html', {'form': form,})   


def edit_bug(request,pk):
    if request.method == 'POST':
        b=Bugs.objects.get(pk=pk)
        form = BugForm(request.POST,instance = b)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/account/') 
    else:
            form=BugForm()
    return render(request, 'PyBugs/edit_bug.html', {'form': form,})        


def del_bug(request,pk):
    b=Bugs.objects.get(pk=pk)
    b.delete()
    return HttpResponseRedirect('/account/') 