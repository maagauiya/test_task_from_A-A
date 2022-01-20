from django.shortcuts import redirect, render
from .models import*
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

def auth(request):
    if request.POST.get('auth'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list/{}'.format(user.pk))
        else:
            return render(request,'todolist/auth.html')
    else:
        return render(request,'todolist/auth.html')

def index(request,userid,*args, **kwargs):
    tasks= Todolist.objects.filter(userid=userid)
    context={
        "tasks" : tasks,
    }
    if request.POST.get('create'):
        taskname = request.POST.get('taskname')
        task = Todolist()
        task.task_text=taskname
        task.status=2
        task.userid=userid
        task.save()
    elif request.POST.get('refresh'):
        print(3)
        return render(request,'todolist/main.html',context=context)
    elif request.POST.get('update'):
        t_upd = Todolist.objects.get(id=request.POST.get("prikey"))
        t_upd.task_text = request.POST.get("old_task") 
        t_upd.status= request.POST.get("option1")
        t_upd.save()

    elif request.POST.get('delete'):
        t_del = Todolist.objects.get(id=request.POST.get("prikey"))
        t_del.delete()
    return render(request,'todolist/main.html',context=context)




