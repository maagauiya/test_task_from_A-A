import json
from django.core import serializers
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import json 
from django.forms.models import model_to_dict
from .models import*
from django.core import serializers
# Create your views here.

def index(request):
    tasks= Todolist.objects.all()
    context={
        "tasks" : tasks,
    }
    if request.method=='POST':
        if request.POST.get('create'):
            taskname = request.POST['taskname']
            task = Todolist()
            task.task_text=taskname
            task.status=2
            task.save()
        elif request.POST.get('refresh'):
            return render(request,'todolist/main.html',context=context)
        elif request.POST.get('update'):
            t_upd = Todolist.objects.get(id=request.POST["prikey"])
            t_upd.task_text = request.POST["old_task"] 
            t_upd.status= request.POST["option1"]
            t_upd.save()

        elif request.POST.get('delete'):
            t_del = Todolist.objects.get(id=request.POST["prikey"])
            t_del.delete()
    return render(request,'todolist/main.html',context=context)
