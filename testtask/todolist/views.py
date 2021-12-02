from django.shortcuts import render
from .models import*
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
