from django.shortcuts import render, HttpResponse
from home.models import Task
def home(request):
    context ={
            'succesS': False,
            'name' : 'harry'
        }
    # return HttpResponse('working')
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        ins=Task(taskTitle = title, taskdesc= desc)
        ins.save()
        context ={
            'success': True
        }
    return render(request, 'index.html',context)

def task(request):
    allTasks = Task.objects.all()
    context = {
        'tasks' : allTasks, 
    }
    for item in allTasks:
        print(item.taskdesc)
    return render(request,'task.html',context)
